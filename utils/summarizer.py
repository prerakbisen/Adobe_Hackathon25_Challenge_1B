from transformers import pipeline
import os

# Using a small quantized model
model_path = os.path.join("models", "tiny_model")

summarizer_pipeline = pipeline("summarization", model=model_path, device=-1)

def summarize_sections(sections, persona, job):
    summarized = []
    for section in sections:
        prompt = f"As a {persona} preparing to {job}, summarize:\n{section['content']}"
        summary = summarizer_pipeline(prompt, max_length=80, min_length=30, do_sample=False)[0]['summary_text']
        section["summary"] = summary
        summarized.append(section)
    return summarized