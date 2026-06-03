# Semantic Search Engine using FAISS

## Overview

This project demonstrates how to build a simple Semantic Search Engine using **Sentence Transformers** and **FAISS (Facebook AI Similarity Search)**.

Instead of matching exact keywords, semantic search understands the meaning of a query and retrieves the most relevant information using vector embeddings.

This is the same retrieval concept used in modern **Retrieval-Augmented Generation (RAG)** systems.

---

## Objectives

- Generate embeddings using Sentence Transformers
- Store embeddings in FAISS
- Perform semantic similarity search
- Retrieve the Top-K most relevant results
- Build an interactive command-line search application

---

## Technologies Used

- Python
- Sentence Transformers
- FAISS
- NumPy

---

## Installation


### Install Dependencies

```bash
pip install sentence-transformers faiss-cpu numpy
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
faiss-semantic-search/
│
├── semantic_search.py
├── theory_answers.md
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses a small knowledge base of customer-support-related sentences:

- Password reset
- Billing information
- Account management
- Login issues
- Refund requests
- Subscription plans
- Security settings
- Account deletion

Example:

```python
knowledge_base = [
    "To reset your password, click on the forgot password link on the login page.",
    "Users can update their billing information from the account settings page.",
    "If your account is locked, contact customer support for assistance.",
    ...
]
```

---

## Step 1: Generate Embeddings

The project uses the pretrained model:

```python
all-MiniLM-L6-v2
```

This model generates:

```text
384-dimensional embeddings
```

Example:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    knowledge_base,
    convert_to_numpy=True
)
```

Output:

```text
(10, 384)
```

---

## Step 2: Build FAISS Index

Create a FAISS index:

```python
index = faiss.IndexFlatL2(384)
```

Normalize embeddings:

```python
faiss.normalize_L2(embeddings)
```

Add vectors:

```python
index.add(embeddings)
```

Check total vectors:

```python
print(index.ntotal)
```

Output:

```text
10
```

---

## Step 3: Semantic Search

Convert the user query into an embedding:

```python
query_embedding = model.encode(
    [query],
    convert_to_numpy=True
)
```

Normalize query vector:

```python
faiss.normalize_L2(query_embedding)
```

Search:

```python
distances, indices = index.search(
    query_embedding,
    k=3
)
```

---

## Example Queries

### Query 1

```text
I forgot my password
```

Results:

```text
1. To reset your password, click on the forgot password link on the login page.
2. Login issues can be resolved by clearing browser cookies and cache.
3. If your account is locked, contact customer support for assistance.
```

---

### Query 2

```text
How can I update payment details?
```

Results:

```text
1. Users can update their billing information from the account settings page.
2. Subscription plans can be upgraded from the billing dashboard.
3. Payment failures may occur due to insufficient account balance.
```

---

### Query 3

```text
Unable to login to my account
```

Results:

```text
1. Login issues can be resolved by clearing browser cookies and cache.
2. If your account is locked, contact customer support for assistance.
3. Two-factor authentication improves account security.
```

---

## Interactive CLI

Run:

```bash
python semantic_search.py
```

Example:

```text
Ask a question (or type exit):
```

Input:

```text
How do I reset my password?
```

Output:

```text
Rank   Score      Matched Sentence

1      0.4213     To reset your password, click on the forgot password link on the login page.
2      0.8421     Login issues can be resolved by clearing browser cookies and cache.
3      0.9578     If your account is locked, contact customer support for assistance.
```

Exit:

```text
exit
```

---

## Why Normalize Embeddings?

Normalization converts vectors to unit length.

```python
faiss.normalize_L2(embeddings)
```

Benefits:

- Enables cosine similarity behavior
- Removes magnitude differences
- Improves semantic retrieval quality

---

## FAISS Workflow

```text
Knowledge Base
       │
       ▼
Sentence Transformer
       │
       ▼
Embeddings (384-D)
       │
       ▼
Normalize
       │
       ▼
FAISS Index
       │
       ▼
User Query
       │
       ▼
Query Embedding
       │
       ▼
Similarity Search
       │
       ▼
Top-K Results
```

---

## Applications

Semantic search is widely used in:

- RAG Applications
- Chatbots
- Customer Support Systems
- Document Search
- Enterprise Knowledge Bases
- Recommendation Systems
- Question Answering Systems

---

## Theory Questions

Detailed answers can be found in:

```text
theory_answers.md
```

Topics covered:

- IndexFlatL2 vs IndexFlatIP
- Cosine Similarity
- Embedding Normalization
- Approximate Nearest Neighbour (ANN) Search

---

## Key Learning Outcomes

After completing this project, you will understand:

- What embeddings are
- How sentence transformers work
- How FAISS stores vectors
- Semantic similarity search
- Vector databases
- Retrieval systems used in RAG applications

---

## Author

**G. Vardhan**

AI/ML Engineer | Generative AI Enthusiast

GitHub: https://github.com/ganugulavardhan-svg