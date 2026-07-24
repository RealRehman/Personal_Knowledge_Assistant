from utils.document_reader import read_documents
from utils.chunking import chunk_text

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

    # Print chunks of the current document
    for j, chunk in enumerate(chunks, start=1):
        print(f"Chunk {j}:")
        print(chunk)
        print("-" * 40)

print("\n========================================")
print(f"Total Documents: {len(documents)}")
print(f"Total Chunks: {len(all_chunks)}")
print("========================================")

# Optional: Print first 5 chunks
print("\nFirst 5 Chunks:\n")

for i, chunk in enumerate(all_chunks[:5], start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 40)