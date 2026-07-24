from utils.search import search_documents

print("\n========== Personal Knowledge Assistant ==========\n")

while True:

    query = input("Ask a question (or type 'exit'): ")

    if query.lower() == "exit":
        print("\nGoodbye! 👋")
        break

    results = search_documents(query)

    print("\nMost Relevant Chunks:\n")

    for i, document in enumerate(results["documents"][0], start=1):
        print(f"Result {i}:")
        print(document)
        print("-" * 60)