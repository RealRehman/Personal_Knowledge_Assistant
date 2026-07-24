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


def read_pdf():
    pdf = PdfReader("documents/resume.pdf")

    print(f"Total pages: {len(pdf.pages)}")

    first_page = pdf.pages[0]

    text = first_page.extract_text()

    print("\n----- First Page -----\n")
    print(text)

read_documents()
read_pdf()