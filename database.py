from sqlmodel import SQLModel, create_engine

sqlite_file = "books.db"
engine = create_engine(f"sqlite:///{sqlite_file}", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)