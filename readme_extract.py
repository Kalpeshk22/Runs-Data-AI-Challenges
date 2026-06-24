from docx import Document

doc = Document("README.docx")

for p in doc.paragraphs:
    text = p.text.strip()
    if text:
        print(text)