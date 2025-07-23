from fastapi import FastAPI
from routers import books
from database import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="Knižná polička", lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Vitajte v API Knižná polička!"}

app.include_router(books.router)