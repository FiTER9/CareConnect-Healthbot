import os
import chainlit as cl
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from typing import Optional, List, Any
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Constants
DB_FAISS_PATH = os.path.join(os.getcwd(), 'vectorstore', 'db_faiss')
MODEL_NAME = "Qwen/Qwen-1_8B-Chat"  # 使用轻量版本
MODEL_TYPE = "qwen"

# Custom prompt for QA
custom_prompt_template = """请根据以下信息回答用户的问题。
如果你不知道答案，请直接说"我不知道"，不要编造答案。

上下文信息: {context}
问题: {question}

请只返回有用的答案，不要包含其他内容。
有用的答案:
"""

# Custom Qwen LLM wrapper
class QwenLLM(LLM):
    model: Any = None
    tokenizer: Any = None
    max_new_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.8

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"Loading Qwen model: {MODEL_NAME}")
        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )

        # 使用 CPU 或 GPU
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")

        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="auto" if device == 'cuda' else None,
            trust_remote_code=True,
            torch_dtype=torch.float16 if device == 'cuda' else torch.float32
        ).eval()

        if device == 'cpu':
            self.model = self.model.float()

        print("Qwen model loaded successfully!")

    @property
    def _llm_type(self) -> str:
        return "qwen"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        try:
            response, history = self.model.chat(
                self.tokenizer,
                prompt,
                history=None,
                max_new_tokens=self.max_new_tokens,
                temperature=self.temperature,
                top_p=self.top_p
            )
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return "抱歉，生成回答时出现错误。"

# Set custom prompt for QA
def set_custom_prompt():
    print("Setting custom prompt template...")
    return PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

# Load the language model
def load_llm():
    print("Loading Qwen LLM...")
    return QwenLLM(
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.8
    )

# Create QA Bot
def qa_bot():
    print("Creating QA bot...")
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': device}
    )
    print(f"Loading FAISS database from: {DB_FAISS_PATH}")
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    print("FAISS database loaded successfully.")
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': qa_prompt}
    )

# Chainlit handlers
@cl.on_chat_start
async def start():
    print("Starting chat session...")
    chain = qa_bot()
    cl.user_session.set("chain", chain)
    print("Bot initialized and session data set.")
    await cl.Message(content="您好！👋 欢迎使用 CareConnect 医疗健康助手（通义千问版）。我可以帮您解答各种健康和医疗相关的问题。请问有什么可以帮助您的？").send()
    print("Greeting message sent.")

@cl.on_message
async def main(message: cl.Message):
    print("Received message:", message.content)
    chain = cl.user_session.get("chain")
    conversation_context = message.content

    try:
        # Generate response using the LLM
        print("Generating response using Qwen...")
        result = await cl.make_async(chain)({"query": conversation_context})
        print("Response generated.")
        answer = result.get("result", "抱歉，我无法找到答案。")
        sources = result.get("source_documents", [])

        # Format the sources
        formatted_sources = "\n\n**信息来源：**\n" if sources else "\n未找到相关来源。"
        for doc in sources:
            source_name = doc.metadata.get('source', '未知来源')
            page_number = doc.metadata.get('page', '未知')
            formatted_sources += f"- {source_name} (第 {page_number} 页)\n"

        # Combine the answer with formatted sources
        final_output = f"{answer}{formatted_sources}"

        # Send the response
        print("Sending response...")
        await cl.Message(content=final_output).send()
        print("Response sent.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        await cl.Message(content=f"抱歉，处理您的问题时出现错误：{str(e)}").send()
