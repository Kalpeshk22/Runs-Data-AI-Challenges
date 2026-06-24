from docx import Document

doc = Document("submission_spec.docx")

with open("submission_spec.txt", "w", encoding="utf-8") as f:
    for p in doc.paragraphs:
        text = p.text.strip()
        if text:
            f.write(text + "\n")