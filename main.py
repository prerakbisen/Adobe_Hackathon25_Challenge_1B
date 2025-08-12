import os
import json
import time
from datetime import datetime
from utils.pdf_parser import extract_pdf_content
from utils.summarizer import summarize_sections
from utils.section_ranker import rank_sections
from utils.json_builder import build_output_json

INPUT_JSON = "input.json"
INPUT_DIR = "data/input_pdfs"
OUTPUT_DIR = "data/output"

def main():
    start_time = time.time()
    

    # Load input.json
    if not os.path.exists(INPUT_JSON):
        raise FileNotFoundError("input.json not found!")
    
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        config_data = json.load(f)

    challenge_info = config_data.get("challenge_info", {})
    persona = config_data.get("persona", {}).get("role", "Analyst")
    job_to_be_done = config_data.get("job_to_be_done", {}).get("task", "Summarize documents")
    documents = config_data.get("documents", [])
    

    
    # Validate documents
    pdf_files = []
    for doc in documents:
        filename = doc.get("filename")
        if not filename:
            print("Warning: Missing filename in input.json document entry.")
            continue
        path = os.path.join(INPUT_DIR, filename)
        if os.path.exists(path):
            pdf_files.append({"path": path, "title": doc.get("title", filename)})
        else:
            print(f"Warning: {filename} not found in {INPUT_DIR}")

    if not pdf_files:
        print("No valid PDF documents found!")
        return
        

    
    # Extract and process
    extracted_sections = []
    for pdf in pdf_files:
        sections = extract_pdf_content(pdf["path"])
        for sec in sections:
            sec["doc_title"] = pdf["title"]
        extracted_sections.extend(sections)
        

    summarized_sections = summarize_sections(extracted_sections, persona=persona, job=job_to_be_done)
    ranked_sections = rank_sections(summarized_sections)

    # Build output JSON
    output_json = build_output_json(
        challenge_info=challenge_info,
        documents=[d["filename"] for d in documents],
        persona=persona,
        job_to_be_done=job_to_be_done,
        ranked_sections=ranked_sections
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"analysis_{int(time.time())}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print(f"Analysis complete. Output saved to {output_path}")
    print(f"Execution time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
                          main()

