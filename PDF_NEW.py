import ollama
import gradio as gr

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


vector_db = None


def load_pdf(file):
    try:
        loader = PyPDFLoader(file.name)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(pages)

        print("Chunks created:", len(chunks))

        if len(chunks) == 0:
            return None

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        db = Chroma.from_documents(chunks, embeddings)

        return db

    except Exception as e:
        print("PDF loading error:", e)
        return None


def upload_pdf(file):
    global vector_db

    vector_db = load_pdf(file)

    if vector_db is None:
        return "❌ Failed to load PDF. Make sure it contains readable text."

    return "✅ PDF loaded successfully! You can now ask questions."


def chat(message, history):
    global vector_db

    if vector_db is None:
        return "⚠ Please upload a PDF first."

    try:
        docs = vector_db.similarity_search(message, k=3)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{message}
"""

        response = ollama.chat(
            model="phi",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        print("Chat error:", e)
        return "⚠ AI failed to generate response."


with gr.Blocks() as demo:

    gr.Markdown("# 📄 Local PDF AI (Ollama + Phi)")

    file = gr.File(label="Upload your PDF")
    status = gr.Textbox(label="Status")

    file.upload(upload_pdf, file, status)

    chatbot = gr.ChatInterface(chat)

demo.launch()