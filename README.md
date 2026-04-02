# CareConnect Medical Chatbot 🏥

An intelligent, interactive medical chatbot designed to assist users with health-related queries. This project leverages cutting-edge tools and technologies, including LangChain for conversational AI, Chainlit for the interface, and FAISS for efficient document retrieval, ensuring an intuitive and seamless user experience.

---

## ✨ Features
- **Natural Language Understanding**: Understands user queries in natural language, ensuring smooth interaction.
- **Interactive Interface**: A user-friendly interface built using Chainlit for seamless communication.
- **Health-Related Insights**: Provides reliable and insightful responses to medical queries based on your knowledge base.
- **Scalable Backend**: Efficient document retrieval powered by FAISS vector database.
- **Custom Knowledge Base**: Enhanced responses through integration with curated medical datasets (PDFs).
- **Local LLM**: Uses Llama-2-7B-Chat model for privacy-focused, offline operation.

---

## 🛠️ Technologies Used
- **LangChain**: Framework for building conversational AI with modular components.
- **Chainlit**: Modern UI framework for building chat applications.
- **FAISS**: Efficient vector search for quick and accurate document retrieval.
- **Llama-2-7B-Chat**: Open-source large language model for generating responses.
- **HuggingFace Transformers**: For embeddings and model management.
- **PyTorch**: Deep learning framework for model inference.
- **Docker**: Containerization for easy deployment and scalability.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or above**
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Docker** (optional, for containerized deployment)
- **At least 8GB RAM** (16GB recommended for better performance)
- **10GB+ free disk space** (for models and dependencies)

---

## 🚀 Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/CareConnect-Healthbot.git
cd CareConnect-Healthbot
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install all required packages including:
- chainlit
- langchain-community
- langchain-huggingface
- torch
- faiss-cpu
- ctransformers
- sentence-transformers
- pydantic
- pypdf

### Step 4: Prepare Medical Knowledge Base

**Important**: The chatbot needs medical PDF documents to function properly.

1. **Add PDF documents** to the `data/` directory:
   ```bash
   # The data/ directory has been created for you
   # Add your medical PDF files here
   ```

2. **Recommended document types**:
   - Medical textbooks
   - Disease treatment guidelines
   - Drug information leaflets
   - Health education materials
   - Medical research papers

3. **Example sources** (ensure you have proper licenses):
   - Public health resources
   - Open-access medical journals
   - Government health department publications
   - Medical education materials

⚠️ **Note**: Make sure you have the legal right to use these documents.

### Step 5: Generate Vector Database

Once you have added PDF files to the `data/` directory, run:

```bash
python ingest.py
```

This script will:
- Load all PDF files from the `data/` directory
- Split documents into manageable chunks
- Generate embeddings using sentence-transformers
- Create a FAISS index for fast similarity search
- Save the vector database to `vectorstore/db_faiss/`

**Expected output**:
```
FAISS index created and stored in 'vectorstore/' successfully.
```

### Step 6: Download Language Model

The application uses **Llama-2-7B-Chat-GGML** model (~7GB).

**Option A: Automatic Download (Recommended)**
- The model will be automatically downloaded on first run
- It will be saved to `~/.cache/transformers/`
- This may take 10-30 minutes depending on your internet speed

**Option B: Manual Download**
```bash
# Download from HuggingFace
# Visit: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
# Download the model file and place it in ~/.cache/transformers/
```

### Step 7: Run the Chatbot

Start the Chainlit application:

```bash
chainlit run chainlit_app.py --host 0.0.0.0 --port 8000
```

**Expected output**:
```
Chainlit: Your app is available at http://localhost:8000
```

### Step 8: Access the Application

Open your web browser and navigate to:
```
http://localhost:8000
```

You should see the CareConnect chatbot interface. Start asking medical questions!

---

## 💡 Usage Guide

1. **Launch the Application**: Run `chainlit run chainlit_app.py`
2. **Open Browser**: Navigate to `http://localhost:8000`
3. **Start Chatting**: Type your medical query in the chat interface
4. **Get Responses**: The bot will search the knowledge base and provide answers with source citations

### Example Queries:
- "What are the symptoms of diabetes?"
- "How to treat a common cold?"
- "What is the recommended dosage for aspirin?"
- "Explain the causes of hypertension"

---

## 🐳 Deployment with Docker

### Build the Docker Image
```bash
docker build -t careconnect-healthbot .
```

### Run the Docker Container
```bash
docker run -p 8000:8000 careconnect-healthbot
```

### Access the Application
Open your browser and navigate to `http://localhost:8000`

---

## 📁 Project Structure

```
CareConnect-Healthbot/
├── chainlit_app.py          # Main Chainlit application
├── ingest.py                # Script to create vector database
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── data/                   # Medical PDF documents (add your files here)
│   └── README.md          # Instructions for adding documents
└── vectorstore/            # FAISS vector database (generated)
    └── db_faiss/          # FAISS index files
```

---

## ⚙️ Configuration

### Environment Variables

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

Key configurations:
- `MODEL_NAME`: LLM model to use
- `EMBEDDING_MODEL`: Embedding model for vector search
- `MAX_NEW_TOKENS`: Maximum tokens in response
- `TEMPERATURE`: Response creativity (0.0-1.0)
- `CHUNK_SIZE`: Document chunk size for processing

---

## 🔧 Troubleshooting

### Issue: "No PDF files found in data/"
**Solution**: Add PDF documents to the `data/` directory and run `python ingest.py`

### Issue: "FAISS index not found"
**Solution**: Run `python ingest.py` to generate the vector database

### Issue: "Model download failed"
**Solution**:
- Check your internet connection
- Manually download from HuggingFace
- Ensure you have enough disk space (~10GB)

### Issue: "Out of memory error"
**Solution**:
- Close other applications
- Use a smaller model
- Reduce `MAX_NEW_TOKENS` in configuration
- Use CPU instead of GPU if memory is limited

### Issue: "Slow response times"
**Solution**:
- Use GPU if available (requires CUDA setup)
- Reduce document chunk size
- Limit the number of retrieved documents (reduce `k` value)

---

## 🎯 Project Highlights

1. **Custom Model Deployment**: Integrates a tailored AI model for domain-specific responses
2. **Efficient Search Mechanism**: Utilizes FAISS for fast and accurate query handling
3. **Scalable Design**: Built with components that allow easy scaling and feature expansion
4. **Privacy-Focused**: Runs completely offline once models are downloaded
5. **Source Attribution**: Provides citations for all responses

---

## 📊 Performance Notes

- **First Run**: May take 10-30 minutes to download models
- **Subsequent Runs**: Starts in 30-60 seconds
- **Response Time**: 5-15 seconds per query (CPU), 1-3 seconds (GPU)
- **Memory Usage**: 4-8GB RAM during operation
- **Disk Space**: ~10GB for models and dependencies

---

## ⚠️ Important Disclaimers

1. **Not a Substitute for Professional Medical Advice**: This chatbot is for informational purposes only and should not replace consultation with qualified healthcare professionals.

2. **Accuracy Depends on Knowledge Base**: The quality of responses depends entirely on the PDF documents you provide.

3. **No Personal Health Information**: Do not input personal health information or use for diagnosis.

4. **Compliance**: Ensure your use complies with local healthcare regulations and data privacy laws (HIPAA, GDPR, etc.).

5. **Model Limitations**: AI models can make mistakes. Always verify critical medical information.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LangChain** for the conversational AI framework
- **Chainlit** for the beautiful chat interface
- **Meta AI** for the Llama-2 model
- **Facebook AI** for FAISS vector search
- **HuggingFace** for model hosting and transformers library

---

## 📧 Contact & Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

---

## 🗺️ Roadmap

- [ ] Add support for multiple languages
- [ ] Implement conversation history
- [ ] Add user authentication
- [ ] Support for more document formats (DOCX, TXT, HTML)
- [ ] Integration with medical APIs
- [ ] Voice input/output support
- [ ] Mobile app version
- [ ] Fine-tuning on medical datasets

---

**Made with ❤️ for better healthcare accessibility**
