import pytest
from models import Book
import crud
from database import create_db_and_tables

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    create_db_and_tables()

def test_create_and_get_book():
    book = Book(title="Test", author="Author", year=2023, genre="Fiction")
    created = crud.create_book(book)
    assert created.id is not None
    fetched = crud.get_book(created.id)
    assert fetched.title == "Test"

def test_update_book():
    book = Book(title="UpdateTest", author="Author", year=2023, genre="Fiction")
    created = crud.create_book(book)
    updated = crud.update_book(created.id, {"title": "Updated"})
    assert updated.title == "Updated"

def test_delete_book():
    book = Book(title="DeleteTest", author="Author", year=2023, genre="Fiction")
    created = crud.create_book(book)
    result = crud.delete_book(created.id)
    assert result is True
    assert crud.get_book(created.id) is None

def test_get_books():
    books = crud.get_books()
    assert isinstance(books, list)