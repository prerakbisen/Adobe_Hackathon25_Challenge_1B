from PyPDF2 import PdfReader

def extract_pdf_content(pdf_path):
    reader = PdfReader(pdf_path)
    sections = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            # Heuristically split by headings (e.g., all-caps or numbered titles)
            parts = text.split("\n")
            for idx, part in enumerate(parts):
                if len(part.strip()) > 5:  # basic filtering
                    sections.append({
                        "document": pdf_path.split("/")[-1],
                        "page": page_num + 1,
                        "title": part[:80],
                        "content": part
                    })
    return sections