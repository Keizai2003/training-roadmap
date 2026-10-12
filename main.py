from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

book = ""

class Book(BaseModel):
    book: str

@app.post("/book")
def create(payload: Book):
    global book
    book = payload.book

@app.get("/book")
def lovely_book():
    return f"любимая книга: {book}"