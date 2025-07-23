from fastapi import APIRouter, HTTPException, Query, UploadFile, File
from models import Book
from schemas import BookCreate, BookRead, BookUpdate
import crud, os, shutil

router = APIRouter(prefix="/books", tags=["Books"])

# zoznam knih
@router.get("/", response_model=list[BookRead])
def read_books(
    q: str = Query(None, description="Vyhľadávanie podľa názvu"),
    genre: str = None,
    author: str = None,
    offset: int = 0,
    limit: int = 10
):
    return crud.get_books(query=q, genre=genre, author=author, offset=offset, limit=limit)

# detail knihy
@router.get("/{book_id}", response_model=BookRead)
def read_books(book_id: int):
    book = crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Kniha nenájdená.")
    return book

# vytvorenie knihy
@router.post("/", response_model=BookRead, status_code=201)
def create_new_book(book: BookCreate):
    new_book = Book(**book.dict())
    return crud.create_book(new_book)

# uprava knihy
@router.put("/{book_id}", response_model=BookRead)
def update_existing_book(book_id: int, book_data: BookUpdate):
    updated = crud.update_book(book_id, book_data.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Kniha nenájdená.")
    return updated

# odstranenie knihy
@router.delete("/{book_id}")
def delete_book(book_id: int):
    success = crud.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Kniha nenájdená.")
    return {"detail": "Kniha bola úspešne odstránená."}

# upload fotky
@router.post("/upload-cover/")
def upload_cover_image(book_id: int, file: UploadFile = File(...)):
    book = crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Kniha nenájdená.")

    # Uloženie súboru
    os.makedirs("covers", exist_ok=True)
    file_location = f"covers/{book_id}_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Aktualizácia knihy o cestu k obálke
    crud.update_book(book_id, {"cover_url": file_location})

    return {"detail": "Obálka bola úspešne nahraná.", "cover_url": file_location}