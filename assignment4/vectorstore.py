import chromadb
from sentence_transformers import SentenceTransformer
import uuid

client = chromadb.PersistentClient(path="./chroma_db")

documents_collection = client.get_or_create_collection(
    name="documents"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def load_documents():

    if documents_collection.count() > 0:
        return

    with open(
        "data/client_documents.txt",
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    chunks = text.split("\n")

    for chunk in chunks:

        if not chunk.strip():
            continue

        embedding = embedding_model.encode(
            chunk
        ).tolist()

        documents_collection.add(
            ids=[str(uuid.uuid4())],
            documents=[chunk],
            embeddings=[embedding]
        )