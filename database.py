import sqlite3

DB_NAME = "student_support.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

def save_conversation(question, answer):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO conversations(question, answer) VALUES (?, ?)", (question, answer))

def get_previous_conversations(limit=5):
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            "SELECT question, answer FROM conversations ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
    return list(reversed(rows))
