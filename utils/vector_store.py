import chromadb


def store_embeddings(chunks, embeddings):
    """
    Stores text chunks and their embeddings in ChromaDB.
    """

    # Create a persistent database
    client = chromadb.PersistentClient(path="vector_db")

    # Create (or get) a collection
    collection = client.get_or_create_collection(
        name="knowledge_base"
    )

    # Generate IDs for each chunk
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Store everything
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print("\n✅ Embeddings stored successfully!")
    print(f"Total Stored: {collection.count()}")