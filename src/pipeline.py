import os
import json
from datetime import datetime
from .loader import load_pdf_text
from .extractor import extract_sections
from .summarizer import summarize_page

def analyze_documents(doc_paths, persona, job, keyword_config):
    all_sections = []
    all_analysis = []

    keywords = keyword_config.get(persona, [])

    for doc_path in doc_paths:
        pages = load_pdf_text(doc_path)
        doc_name = os.path.basename(doc_path)
        sections = extract_sections(pages, doc_name, keywords)
        analysis = [{
            "doc": doc_name,
            "page": s["page"],
            "points": summarize_page(pages[s["page"] - 1])
        } for s in sections]
        all_sections.extend(sections)
        all_analysis.extend(analysis)

    return {
        "metadata": {
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.utcnow().isoformat(),
            "documents": [os.path.basename(p) for p in doc_paths]
        },
        "extracted_sections": all_sections,
        "sub_section_analysis": all_analysis
    }