from pathlib import Path
from pypdf import PdfReader

SUPPORTED_FILES = [".pdf", ".txt", ".docx"]


def read_documents():
    documents_path = Path("documents")

    documents = []

    for file in documents_path.iterdir():

        if file.suffix in SUPPORTED_FILES:

            print(f"\n----- {file.name} -----")

            if file.suffix == ".txt":
                content = file.read_text()
                documents.append(content)

            elif file.suffix == ".pdf":
                pdf_text = read_pdf(file)
                documents.append(pdf_text)
    return documents


def read_pdf(file_path):
    pdf = PdfReader(file_path)


    all_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        if text:  
            all_text += text + "\n"

    return all_text

    # first_page = pdf.pages[0]

    # text = first_page.extract_text()

    # return text

