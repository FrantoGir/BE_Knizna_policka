from pydantic import BaseModel, HttpUrl
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: str
    cover_url: Optional[str] = None
    
class BookRead(BookCreate):
    id: int
    
class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
    genre: Optional[str]
    cover_url: Optional[str] = None