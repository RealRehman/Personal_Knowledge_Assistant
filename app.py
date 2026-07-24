from utils.document_reader import read_documents
from utils.chunking import chunk_text

# Read all documents from the documents folder
documents = read_documents()

# Process each document
for i, document in enumerate(documents, start=1):
    print(f"\n========== Document {i} ==========\n")

    chunks = chunk_text(document)

    for j, chunk in enumerate(chunks, start=1):
        print(f"Chunk {j}:")
        print(chunk)
        print("-" * 40)