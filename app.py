from pathlib import Path

documents_path = Path("documents")

for file in documents_path.iterdir():
    print(file.name)