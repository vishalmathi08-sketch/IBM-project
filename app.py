from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from database import init_db
from rag.document_loader import process_pdf
from agents.student_support_agent import answer_question

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("pdf")
    if not f or f.filename == "":
        return render_template("index.html", message="Please select a PDF file.")
    if not f.filename.lower().endswith(".pdf"):
        return render_template("index.html", message="Only PDF files are allowed.")
    path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename))
    f.save(path)
    count = process_pdf(path, f.filename)
    return render_template("index.html", message=f"PDF uploaded and indexed successfully ({count} chunks).")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()
    if not question:
        return render_template("index.html", message="Please enter a question.")
    answer, sources = answer_question(question)
    return render_template("answer.html", question=question, answer=answer, sources=sources)

if __name__ == "__main__":
    app.run(debug=True)
