# Local-PDF-AI-Chatbot-Ollama-LangChain-Gradio-
# 📄 Local PDF AI Chatbot (Ollama + LangChain + Gradio)

A **local AI-powered PDF chatbot** that allows users to upload a PDF and ask questions about its content.
The system uses **Retrieval Augmented Generation (RAG)** with a local LLM to provide context-aware answers.

---

## 🚀 Features

* Upload any **PDF document**
* Extracts and processes text automatically
* Creates **vector embeddings** for semantic search
* Uses **ChromaDB** for vector storage
* Retrieves relevant document sections
* Generates answers using **Ollama local LLM**
* Interactive **Gradio web interface**

---

## 🧠 Architecture

```
PDF Upload
    ↓
Text Extraction (PyPDFLoader)
    ↓
Text Chunking (RecursiveCharacterTextSplitter)
    ↓
Embeddings (Sentence Transformers)
    ↓
Vector Database (Chroma)
    ↓
Retriever
    ↓
Local LLM (Ollama - Phi)
    ↓
Answer Generation
```

---

## 🛠 Tech Stack

* **Python**
* **LangChain**
* **ChromaDB**
* **Sentence Transformers**
* **Ollama**
* **Gradio**

---

## 📦 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/pdf-ai-chatbot.git
cd pdf-ai-chatbot
```

---

### 2️⃣ Create environment

```
conda create -n pytorch_env python=3.10
conda activate pytorch_env
```

---

### 3️⃣ Install dependencies

```
pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers gradio ollama pypdf
```

---

### 4️⃣ Install Ollama

Download from:

https://ollama.com

---

### 5️⃣ Download the model

```
ollama pull phi
```

---

## ▶ Running the Application

```
python PDF_NEW.py
```

Then open:

```
http://127.0.0.1:7860
```

Upload a PDF and start asking questions.

---

## 📸 Example Usage

1. Upload a PDF document
2. Ask questions like:

```
What is the document about?
Summarize the key points.
Explain section 3.
```

The AI retrieves relevant content and generates an answer.

---

## 📊 Project Type

This project demonstrates a **Retrieval Augmented Generation (RAG)** pipeline using a **local LLM**.

It showcases how to combine:

* Document processing
* Semantic search
* Vector databases
* Local AI models

---

## 🔮 Future Improvements

* Conversation memory
* Multi-document support
* Faster retrieval
* Streaming responses
* Voice interface
* Web search integration

---


