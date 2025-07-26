from pdfminer.high_level import extract_text

def load_pdf_text(pdf_path):
    text = extract_text(pdf_path)
    pages = text.split('\f')
    return [p.strip() for p in pages if p.strip()]