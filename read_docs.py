from docx import Document

files = [
    "README.docx",
    "job_description.docx",
    "submission_spec.docx",
    "redrob_signals_doc.docx"
]

for file in files:
    print("\n" + "="*80)
    print(file)
    print("="*80)

    doc = Document(file)

    for para in doc.paragraphs[:50]:
        text = para.text.strip()
        if text:
            print(text)