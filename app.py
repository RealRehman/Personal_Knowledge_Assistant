from utils.document_reader import read_documents

read_documents()

from utils.chunking import chunk_text

sample = """Python is easy to learn.
Functions help organize code.
Classes support OOP.
Modules improve reuse.
Packages organize modules."""

chunk_text(sample)