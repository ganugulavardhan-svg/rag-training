import chromadb
from sentence_transformers import SentenceTransformer
import uuid

client = chromadb.PersistentClient(
    path="./chroma_db"
)

memory_collection = client.get_or_create_collection(
    name="memory"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def save_memory(text: str):

    embedding = embedding_model.encode(
        text
    ).tolist()

    memory_collection.add(
        ids=[str(uuid.uuid4())],
        documents=[text],
        embeddings=[embedding]
    )

    return "Memory stored."


def retrieve_memory(query: str):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = memory_collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]

    if not docs:
        return "No memory found."

    return "\n".join(docs)