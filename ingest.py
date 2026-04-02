import os

# Ensure only one OpenMP runtime is used
os.environ["KMP_INIT_AT_FORK"] = "FALSE"  # Prevent issues with subprocesses
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # Allow execution but risks remain

import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Limit PyTorch threads
torch.set_num_threads(1)

DATA_PATH = 'data/'  # Directory containing PDFs
DB_FAISS_PATH = 'vectorstore/db_faiss'  # Directory to save FAISS index

# Create vector database using FAISS
def create_vector_db():
    # Step 1: Load documents
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()

    # Step 2: Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Step 3: Set up embeddings model
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    embeddings = HuggingFaceEmbeddings(
        model_name='shibing624/text2vec-base-chinese',
        model_kwargs={'device': device}
    )

    # Step 4: Create FAISS vector store
    print("Creating FAISS vector store...")
    db = FAISS.from_documents(texts, embeddings)

    # Step 5: Save FAISS index
    db.save_local(DB_FAISS_PATH)

    print(f"FAISS index created and stored in '{DB_FAISS_PATH}' successfully.")

if __name__ == "__main__":
    create_vector_db()
