from vectorstore import (
    documents_collection,
    embedding_model
)


def search_client_documents(query: str):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = documents_collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]

    if not docs:
        return "No relevant documents found."

    return "\n".join(docs)