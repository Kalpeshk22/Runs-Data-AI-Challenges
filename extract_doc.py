from docx import Document

doc = Document("redrob_signals_doc.docx")

with open("redrob_full.txt", "w", encoding="utf-8") as f:
    for para in doc.paragraphs:
        f.write(para.text + "\n")