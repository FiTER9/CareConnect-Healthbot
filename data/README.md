# Medical Knowledge Base

## 📚 Purpose
This directory contains PDF documents that serve as the knowledge base for the medical chatbot.

## 📄 How to Add Documents

1. Place your medical PDF documents in this directory
2. Supported formats: PDF files only
3. Recommended content:
   - Medical textbooks
   - Disease guidelines
   - Drug information
   - Medical research papers
   - Health education materials

## ⚠️ Important Notes

- **Quality Matters**: The quality of responses depends on the quality of documents you provide
- **Copyright**: Ensure you have the right to use these documents
- **Privacy**: Do not include documents with personal health information (PHI)
- **Language**: Documents should be in the language you want the chatbot to respond in

## 🔄 After Adding Documents

After adding or updating PDF files in this directory, you need to regenerate the vector database:

```bash
python ingest.py
```

This will process all PDF files and create/update the FAISS vector database in the `vectorstore/` directory.

## 📝 Example Documents to Include

- General medicine textbooks
- Common diseases and treatments
- First aid guides
- Nutrition and wellness information
- Mental health resources
- Preventive care guidelines

## 🚫 What NOT to Include

- Personal medical records
- Copyrighted materials without permission
- Outdated or inaccurate medical information
- Non-medical content
