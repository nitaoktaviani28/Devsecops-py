from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS untuk frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    cover: str

# Data dummy
books = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008, 
         cover="https://images.unsplash.com/photo-1532012197267-da84d127e765?w=300"),
    Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999,
         cover="https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=300"),
    Book(id=3, title="Design Patterns", author="Gang of Four", year=1994,
         cover="https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=300"),
    Book(id=4, title="Refactoring", author="Martin Fowler", year=1999,
         cover="https://images.unsplash.com/photo-1512820790803-83ca734da794?w=300"),
]

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = next((b for b in books if b.id == book_id), None)
    if book:
        return book
    return {"error": "Book not found"}, 404
