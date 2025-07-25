from sqlmodel import SQLModel, Field
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int
    genre: str
    cover_url: Optional[str] = None