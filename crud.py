from sqlmodel import Session, select
from models import Book
from database import engine

def get_books(query: str = None, genre: str = None, author: str = None, offset: int = 0, limit: int = 10):
    with Session(engine) as session:
        statement = select(Book)
        if query:
            statement = statement.where(Book.title.contains(query))
        if genre:
            statement = statement.where(Book.genre == genre)
        if author:
            statement = statement.where(Book.author == author)
        results = session.exec(statement.offset(offset).limit(limit)).all()
        return results

def get_book(book_id: int):
    with Session(engine) as session:
        return session.get(Book, book_id)

def create_book(book: Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

def update_book(book_id: int, data: dict):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            return None
        for key, value in data.items():
            setattr(book, key, value)
        session.commit()
        session.refresh(book)
        return book

def delete_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if book:
            session.delete(book)
            session.commit()
            return True
        return None