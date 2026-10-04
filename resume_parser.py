from pypdf import PdfReader
from docx import Document


def extract_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = []

    for page in reader.pages:
        text.append(page.extract_text() or "")

    return "\n".join(text)


def extract_docx_text(file_path):
    document = Document(file_path)
    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)


def extract_text(file_path):
    file_path = file_path.lower()

    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)

    if file_path.endswith(".docx"):
        return extract_docx_text(file_path)

    raise ValueError("Unsupported resume format. Use PDF or DOCX.")
