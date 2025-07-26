def extract_sections(pages, doc_name, keywords):
    hits = []
    for i, page in enumerate(pages):
        score = sum(page.lower().count(k.lower()) for k in keywords)
        if score > 0:
            title = page.split("\n")[0][:80]
            hits.append({
                "doc": doc_name,
                "page": i + 1,
                "title": title,
                "rank": score
            })
    return sorted(hits, key=lambda x: x["rank"], reverse=True)