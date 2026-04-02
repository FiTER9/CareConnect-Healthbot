import os
import chainlit as cl
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain_classic.chains import RetrievalQA
import torch

# Constants
DB_FAISS_PATH = os.path.join(os.getcwd(), 'vectorstore', 'db_faiss')
MODEL_NAME = "deepseek-r1:8b" 

# Custom prompt for QA
custom_prompt_template = """使用以下上下文信息来回答用户的问题。
如果你不知道答案，就说你不知道，不要试图编造答案。

上下文: {context}
问题: {question}

只返回有帮助的答案，不要返回其他内容。
有帮助的答案:
"""

# Set custom prompt for QA
def set_custom_prompt():
    print("Setting custom prompt template...")
    return PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

# Load the language model
def load_llm():
    print(f"Loading LLM: {MODEL_NAME}...")
    # 确保你已经安装了 Ollama 并运行了 'ollama pull deepseek-r1:8b'
    return Ollama(
        model=MODEL_NAME,
        temperature=0.5
    )

# Create QA Bot
def qa_bot():
    print("Creating QA bot...")
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    embeddings = HuggingFaceEmbeddings(
        model_name="shibing624/text2vec-base-chinese",
        model_kwargs={'device': device},
        cache_folder=os.path.expanduser("~/.cache/huggingface/hub")
    )
    print(f"Loading FAISS database from: {DB_FAISS_PATH}")
    # Allow dangerous deserialization since we created the DB ourselves
    try:
        db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
        print("FAISS database loaded successfully.")
    except Exception as e:
        print(f"Error loading FAISS database: {e}")
        print("Please run ingest.py first to create the vector database.")
        raise e

    llm = load_llm()
    qa_prompt = set_custom_prompt()
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={'k': 4}),  # 增加到4个文档块
        return_source_documents=True,
        chain_type_kwargs={'prompt': qa_prompt}
    )

# Chainlit handlers
@cl.on_chat_start
async def start():
    print("Starting chat session...")
    try:
        chain = qa_bot()
        cl.user_session.set("chain", chain)
        print("Bot initialized and session data set.")
        await cl.Message(content="您好！👋 欢迎使用 CareConnect 医疗健康助手（Powered by DeepSeek）。我可以帮您解答各种健康和医疗相关的问题。请问有什么可以帮助您的？").send()
        print("Greeting message sent.")
    except Exception as e:
        await cl.Message(content=f"初始化失败: {str(e)}。请确保已运行 ingest.py 并且 Ollama 服务正在运行。").send()

@cl.on_message
async def main(message: cl.Message):
    print("Received message:", message.content)
    chain = cl.user_session.get("chain")
    
    if not chain:
        await cl.Message(content="机器人未正确初始化，请检查后台日志。").send()
        return

    conversation_context = message.content

    try:
        # Generate response using the LLM
        print("Generating response using the LLM...")
        # 使用 make_async 包装同步链，避免阻塞事件循环
        res = await cl.make_async(chain)({"query": conversation_context})
        print("Response generated.")
        
        answer = res.get("result", "抱歉，我无法找到答案。")
        sources = res.get("source_documents", [])

        # Format the sources
        formatted_sources = "\n\n**参考来源:**\n" if sources else "\n未找到相关文档。"
        for doc in sources:
            source_name = doc.metadata.get('source', 'Unknown Source')
            page_number = doc.metadata.get('page', 'N/A')
            formatted_sources += f"- {os.path.basename(source_name)} (页码 {page_number})\n"

        # Combine the answer with formatted sources
        final_output = f"{answer}{formatted_sources}"

        # Send the response
        print("Sending response...")
        await cl.Message(content=final_output).send()
        print("Response sent.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        await cl.Message(content=f"发生错误: {str(e)}").send()
