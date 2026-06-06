# Conversational RAG Assistant with Long-Term Memory

## Overview

This project implements a Conversational Retrieval-Augmented Generation (RAG) Assistant using LangChain, ChromaDB, and Gemini.

The assistant can:

* Search enterprise documents using semantic search
* Retrieve meeting notes
* Store and retrieve long-term memory across sessions
* Maintain short-term conversational context
* Use tools autonomously through an agentic workflow

This solution demonstrates modern AI agent architecture by combining Retrieval-Augmented Generation (RAG), vector databases, memory systems, and tool-calling agents.

---

## Features

### 1. Retrieval-Augmented Generation (RAG)

The assistant retrieves relevant information from a ChromaDB vector database before generating responses.

Benefits:

* Reduces hallucinations
* Provides grounded responses
* Enables enterprise knowledge retrieval

---

### 2. Short-Term Memory

Conversation history is maintained during the current session.

Examples:

* Follow-up questions
* Multi-turn conversations
* Context-aware responses

---

### 3. Long-Term Memory

Important information is stored permanently in a ChromaDB collection.

Examples:

* User preferences
* Client requirements
* Project decisions
* Historical context

Memory persists even after restarting the application.

---

### 4. Agentic Workflow

Instead of directly answering every question, the assistant decides which tool to use.

Available tools:

* Document Search
* Meeting Notes Retrieval
* Memory Retrieval
* Memory Storage

---

## Project Architecture

```text
                    User Query
                         │
                         ▼
                ┌─────────────────┐
                │     Agent       │
                │ Gemini 2.5 Flash│
                └────────┬────────┘
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼

 Document Search    Meeting Notes      Memory Retrieval
       Tool              Tool               Tool
         │                 │                  │
         ▼                 ▼                  ▼

     ChromaDB         Notes File      ChromaDB Memory
         │
         ▼
 Retrieved Context
         │
         ▼
      Response
```

---

## Project Structure

```text
assignment4/
│
├── app.py
├── agent.py
├── vectorstore.py
├── memory_store.py
│
├── chroma_db/
│
├── data/
│   ├── client_documents.txt
│   └── meeting_notes.txt
│
└── tools/
    ├── document_tool.py
    ├── meeting_tool.py
    └── memory_tool.py
```

---

## Technologies Used

* Python
* LangChain
* Google Gemini 2.5 Flash
* ChromaDB
* Sentence Transformers
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd assignment4
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-google-genai
pip install chromadb
pip install sentence-transformers
pip install python-dotenv
```

Or:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## Running the Application

```bash
python app.py
```

Example:

```text
Assistant Ready!

You: What was discussed in the last meeting?

Assistant:
The previous meeting discussed:
- RAG architecture
- ChromaDB implementation
- Monthly reporting requirements
```

---

## Example Conversations

### Document Retrieval

```text
You:
What is the billing cycle?

Assistant:
The billing cycle starts on the first day of every month.
```

---

### Meeting Notes Retrieval

```text
You:
What did we discuss in the last meeting?

Assistant:
The meeting covered RAG architecture, ChromaDB implementation, and reporting requirements.
```

---

### Long-Term Memory Storage

```text
You:
Remember that Client ABC prefers monthly reports.
```

Agent stores the information in ChromaDB memory.

---

### Long-Term Memory Retrieval

```text
You:
What reporting preference does Client ABC have?

Assistant:
Client ABC prefers monthly reports.
```

---

## How Long-Term Memory Works

### Store Memory

```python
save_memory(
    "Client ABC prefers monthly reports."
)
```

### Retrieve Memory

```python
retrieve_memory(
    "reporting preference"
)
```

The memory is converted into embeddings and stored in ChromaDB for semantic retrieval.

---

## Assignment Requirements Mapping

| Requirement              | Implementation                |
| ------------------------ | ----------------------------- |
| RAG                      | ChromaDB + Semantic Retrieval |
| Vector Database          | ChromaDB                      |
| Short-Term Memory        | Chat History                  |
| Long-Term Memory         | ChromaDB Memory Collection    |
| Agentic Workflow         | LangChain Agent               |
| Tool Usage               | 4 Tools                       |
| Multi-turn Conversations | Supported                     |
| Persistent Storage       | ChromaDB                      |

---

## Future Improvements

* Memory summarization
* User-specific memory namespaces
* Hybrid search (keyword + vector)
* Streaming responses
* Web search tool integration
* Multi-agent architecture
* Document upload support

---

## Learning Outcomes

By completing this project, the following concepts are demonstrated:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* Long-Term Memory Systems
* Conversational Memory
* Agentic AI Workflows
* Tool Calling
* Enterprise AI Assistants

---
