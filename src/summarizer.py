def summarize_page(page_text):
    lines = page_text.split("\n")
    return [line.strip() for line in lines if len(line.strip()) > 40][:3]