# AI Student Support Assistant

Project based on the provided IBM SkillsBuild Agentic AI project documentation.

## Features
- PDF upload and processing
- RAG using ChromaDB + Sentence Transformers
- Conversation memory using SQLite
- Agent orchestration
- Local Llama 3.2 via Ollama
- Flask web interface
- Current date, support services and percentage tools

## Setup
1. Install Python 3.10+
2. `python -m venv venv`
3. Activate virtual environment
4. `pip install -r requirements.txt`
5. Install Ollama and run:
   - `ollama pull llama3.2`
6. Start Ollama:
   - `ollama serve`
7. Run:
   - `python app.py`
8. Open http://127.0.0.1:5000

## Note
Scanned PDFs without selectable text may require OCR and are not handled by the base PyPDF pipeline.
