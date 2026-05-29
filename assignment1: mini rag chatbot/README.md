# 🚀 Mini RAG Chatbot (PDF Q&A using Gemini + FAISS)

A lightweight **Retrieval-Augmented Generation (RAG)** chatbot that enables users to ask questions directly from PDF documents using **Google Gemini AI** and **FAISS** for semantic search.

This project is intentionally built without heavy frameworks like LangChain to keep the implementation simple, fast, and dependency-friendly.

---

# 🧠 Workflow

```text
PDF → Text Extraction → Chunking → Embedding Generation → FAISS Indexing → Semantic Search → Gemini Response
```

---

# ✨ Features

* Extract text from PDF documents
* Split content into manageable chunks
* Generate lightweight embeddings
* Store and search embeddings using FAISS
* Perform semantic similarity search
* Retrieve relevant context for queries
* Generate accurate answers with Google Gemini AI

---

# 🛠️ Tech Stack

* Python
* Google Generative AI (Gemini)
* FAISS (Vector Database)
* PyPDF
* NumPy

---

# 📁 Project Structure

```text
mini-rag-chatbot/
│
├── main.py / notebook.ipynb
├── sample.pdf
└── README.md
```

---

# ⚙️ Installation

Install the required dependencies:

```bash
pip install pypdf faiss-cpu numpy google-generativeai
```

---

# 🔑 Gemini API Key Setup

Get your Gemini API key from:

https://aistudio.google.com/app/apikey

Configure the API key in your Python code:

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

# ▶️ Running the Project

Run the Python script or Jupyter Notebook:

```bash
python main.py
```

---

# 📌 Use Case

This project demonstrates the core concepts of a RAG pipeline in a minimal and beginner-friendly way, making it ideal for learning semantic search and AI-powered document question answering.
