from fastapi import FastAPI
from app.model import summarize_text
from app.db import save_entry,get_all_entries

app = FastAPI()

@app.post("/submit")
def submit_entry(text: str):
    summary = summarize_text(text)
    save_entry(text, summary)
    return {"summary": summary}

@app.get("/entries")
def entries():
    return get_all_entries()
