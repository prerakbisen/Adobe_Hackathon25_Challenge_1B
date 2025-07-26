from datetime import datetime

def build_output_json(challenge_info, documents, persona, job_to_be_done, ranked_sections):
    metadata = {
        "challenge_info": challenge_info,
        "input_docs": documents,
        "persona": persona,
        "job_to_be_done": job_to_be_done,
        "timestamp": datetime.utcnow().isoformat()
    }
    return {
        "metadata": metadata,
        "extracted_sections": [
            {
                "document": sec["document"],
                "doc_title": sec.get("doc_title", ""),
                "page": sec["page"],
                "title": sec["title"],
                "importance_rank": sec["importance_rank"],
                "summary": sec["summary"]
            }
            for sec in ranked_sections
        ]
    }
