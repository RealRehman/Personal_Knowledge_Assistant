import chromadb
from sentence_transformers import SentenceTransformer

# Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection("knowledge_base")


def search_documents(query, top_k=3):
    """
    Searches the vector database for the most relevant chunks.
    """

    # Convert the user's question into an embedding
    query_embedding = model.encode(query)

    # Search the vector database
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results