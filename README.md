# Persona-Driven Document Intelligence

This project provides a **persona-driven intelligent document analysis pipeline**. It processes multiple PDF files, extracts key sections, summarizes them based on a defined persona and job-to-be-done, and outputs a structured JSON file.

---

## **Features**
- **Multi-PDF Processing:** Handles 3–10 PDF files at once.
- **Persona-Aware Summarization:** Summaries tailored to a defined role (e.g., *Travel Planner* or *Investor*).
- **Structured JSON Output:** Contains metadata, ranked sections, and subsection analysis.
- **Offline Execution:** CPU-only processing, designed for lightweight environments.
- **Dockerized Deployment:** No need to set up dependencies manually.

---

## **Repository Structure**
```
.
├── Dockerfile                # Docker build configuration
├── main.py                   # Entry point script for PDF analysis
├── input.json                # Input configuration (persona, documents, task)
├── requirements.txt          # Python dependencies
│
├── utils/                    # Helper modules
│   ├── pdf_parser.py         # PDF text extraction logic
│   ├── summarizer.py         # Summarizer (persona-driven)
│   ├── section_ranker.py     # Ranks extracted sections
│   └── json_builder.py       # Builds final JSON output
│
└── data/
    ├── input_pdfs/           # Place input PDFs here
    └── output/               # Generated JSON outputs
```

---

## **Installation & Usage**

### **1. Prerequisites**
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- Place your PDF files inside `data/input_pdfs/`.
- Update `input.json` with:
  - **Persona:** Role (e.g., *Travel Planner*).
  - **Job-to-be-done:** Task to perform (e.g., *Plan a 4-day trip*).
  - **Documents:** List of PDFs with titles.

---

### **2. Build the Docker Image**
From the project root, run:
```bash
docker build -t persona-doc-analyst .
```

---

### **3. Run the Container**
Run the following command to analyze PDFs:
```bash
docker run --rm \
  -v ${PWD}/data/input_pdfs:/app/data/input_pdfs \
  -v ${PWD}/data/output:/app/data/output \
  persona-doc-analyst
```

**For Windows PowerShell:**
```powershell
docker run --rm -v ${PWD}/data/input_pdfs:/app/data/input_pdfs -v ${PWD}/data/output:/app/data/output persona-doc-analyst
```

**For Windows CMD:**
```cmd
docker run --rm -v %cd%\data\input_pdfs:/app/data/input_pdfs -v %cd%\data\output:/app/data/output persona-doc-analyst
```

---

### **4. Output**
The container will generate:
```
data/output/analysis_<timestamp>.json
```
This JSON includes:
- `metadata` (persona, job-to-be-done, input documents, timestamp)
- `extracted_sections` (document, page, title, rank, summary)

---

## **Local Development (Optional)**
If you prefer running the script without Docker:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

---

## **Example `input.json`**
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_002",
    "test_case_name": "travel_planner",
    "description": "France Travel"
  },
  "documents": [
    { "filename": "South of France - Cities.pdf", "title": "South of France - Cities" },
    { "filename": "South of France - Cuisine.pdf", "title": "South of France - Cuisine" }
  ],
  "persona": { "role": "Travel Planner" },
  "job_to_be_done": { "task": "Plan a trip of 4 days for a group of 10 college friends." }
}
```

---
