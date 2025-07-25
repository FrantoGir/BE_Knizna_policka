# Knižná polička – REST API

## Popis

Toto je jednoduché REST API pre správu knižnice postavené na FastAPI. 
Umožňuje evidovať knihy, vyhľadávať, filtrovať, upravovať, mazať a nahrávať obálky kníh. 
Dáta sú uložené v SQLite databáze.

---

## Inštalácia

1. **Klonujte repozitár:**
   ```

   git clone <repo-url>
   cd knizna_policka

   ```

2. **Vytvorte virtuálne prostredie a aktivujte ho:**
   ```

   python -m venv venv
   venv\Scripts\activate

   ```

3. **Nainštalujte závislosti:**
   ```

   pip install fastapi uvicorn sqlmodel pydantic

   ```
---

## Spustenie aplikácie
```

uvicorn main:app --reload

```

Aplikácia bude dostupná na [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

### Knihy

- **GET /books**  
  Zoznam všetkých kníh. Podporuje vyhľadávanie (`q`), filtrovanie (`genre`, `author`) a stránkovanie (`limit`, `offset`).

- **GET /books/{id}**  
  Detail knihy podľa ID.

- **POST /books**  
  Vytvorenie novej knihy.  
  ```json
  {
    "title": "Názov",
    "author": "Autor",
    "year": 2024,
    "genre": "Žáner",
    "cover_url": "http://..."
  }
  ```

- **PUT /books/{id}**  
  Úprava existujúcej knihy.

- **DELETE /books/{id}**  
  Odstránenie knihy.

- **POST /books/upload-cover/**  
  Upload obálky knihy (multipart/form-data, parametre: `book_id`, `file`).  
  Uloží obrázok do priečinka `covers` a aktualizuje cestu v databáze.

---

## Dokumentácia

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Požiadavky

- Python 3.11+
- Pozrite si `requirements.txt` pre zoznam balíčkov:
  ```
  
  pip install -r requirements.txt

  ```

---

## Upload obálky knihy

- Endpoint: **POST /books/upload-cover/**
- Parametre:
  - `book_id` (int, ako query parameter)
  - `file` (obrázok, multipart/form-data)
- Príklad použitia v Postman/Swagger:
  - Vyberte typ požiadavky `form-data`
  - Pole `book_id` nastavte na ID knihy
  - Pole `file` vyberte obrázok
- Obrázky sa ukladajú do priečinka `covers/` a cesta sa uloží do `cover_url` v databáze.
- Prístup k obrázku je cez lokálnu cestu (napr. `covers/3_nazov.jpg`).

---

## Reset databázy

Ak chcete začať s čistou databázou, vymažte súbor `books.db` a reštartujte aplikáciu.

---

## Testovanie

Testy pokrývajú:
- Vytvorenie knihy
- Získanie knihy
- Aktualizáciu knihy
- Odstránenie knihy
- Získanie zoznamu kníh

Spustenie testov:
```
pytest testing.py

```

---

## Štruktúra projektu

```
main.py
models.py
schemas.py
crud.py
database.py
routers/
    books.py
covers/
books.db
```
---

## Poznámky

- Dáta sú uložené v `books.db` (SQLite).
- Obálky kníh sa ukladajú do priečinka `covers`.
- API automaticky generuje OpenAPI dokumentáciu.

---