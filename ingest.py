from utils.document_reader import read_documents
from utils.chunking import chunk_text
from utils.embeddings import create_embeddings
from utils.vector_store import store_embeddings

print("\n========== Document Ingestion Started ==========\n")

# Read all documents
documents = read_documents()

# Store chunks from all documents
all_chunks = []

# Process each document
for document in documents:
    chunks = chunk_text(document)
    all_chunks.extend(chunks)

# Create embeddings
embeddings = create_embeddings(all_chunks)

# Store in ChromaDB
store_embeddings(all_chunks, embeddings)

print("\n========== Ingestion Summary ==========")
print(f"Total Documents : {len(documents)}")
print(f"Total Chunks    : {len(all_chunks)}")
print(f"Total Embeddings: {len(embeddings)}")

if len(embeddings) > 0:
    print(f"Embedding Dimension: {len(embeddings[0])}")

print("\n✅ Ingestion Completed Successfully!")