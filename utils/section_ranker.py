def rank_sections(sections):
    # Rank sections by length of content as a proxy for importance
    # (Can be replaced with TF-IDF or embeddings if needed)
    for sec in sections:
        sec["importance_rank"] = len(sec.get("content", ""))  # simple heuristic
    sections.sort(key=lambda x: x["importance_rank"], reverse=True)
    return sections