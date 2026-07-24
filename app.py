from utils.document_reader import read_documents
from utils.chunking import chunk_text
from utils.embeddings import create_embeddings

# Read all documents
documents = read_documents()

# Store chunks from all documents
all_chunks = []

# Process each document
for i, document in enumerate(documents, start=1):
    print(f"\n========== Document {i} ==========\n")

    chunks = chunk_text(document)

    # Add all chunks to the master list
    all_chunks.extend(chunks)

# Create embeddings AFTER all chunks are collected
embeddings = create_embeddings(all_chunks)

print("\n========== Embedding Summary ==========")
print(f"Total Documents: {len(documents)}")
print(f"Total Chunks: {len(all_chunks)}")
print(f"Total Embeddings: {len(embeddings)}")

if len(embeddings) > 0:
    print(f"Embedding Dimension: {len(embeddings[0])}")