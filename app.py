from pathlib import Path

documents_path = Path("documents")

SUPPORTED_FILES = [".pdf", ".txt", ".docx"]

for file in documents_path.iterdir():
    if file.suffix in SUPPORTED_FILES:

        print(f"\n----- {file.name} -----")

        if file.suffix == ".txt":
            content = file.read_text()
            print(content)