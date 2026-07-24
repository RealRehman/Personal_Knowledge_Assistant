from pathlib import Path
from pypdf import PdfReader

SUPPORTED_FILES = [".pdf", ".txt", ".docx"]


def read_documents():
    documents_path = Path("documents")

    for file in documents_path.iterdir():

        if file.suffix in SUPPORTED_FILES:

            print(f"\n----- {file.name} -----")

            if file.suffix == ".txt":
                content = file.read_text()
                print(content)

            elif file.suffix == ".pdf":
                read_pdf(file)


def read_pdf(file_path):
    pdf = PdfReader(file_path)

    print(f"Total pages: {len(pdf.pages)}")

    first_page = pdf.pages[0]

    text = first_page.extract_text()

    print(text)

read_documents()
