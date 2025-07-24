# Knižná polička – REST API

## Popis

Toto je jednoduché REST API pre správu knižnice postavené na FastAPI.  
Umožňuje evidenciu kníh, vyhľadávanie, filtrovanie, úpravu, mazanie a nahrávanie obálok kníh.  
Dáta sú uložené v databáze SQLite.

---

## Inštalácia

**Klonujte repozitár:**
```bash
git clone <repo-url>
cd knizna_policka
```

**Vytvorte virtuálne prostredie a aktivujte ho:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

**Nainštalujte závislosti:**
```bash
pip install fastapi uvicorn sqlmodel pydantic
```

alebo (pre všetky balíčky):
```bash
pip install -r requirements.txt
```

---

## Spustenie aplikácie

```bash
uvicorn main:app --reload
```

Aplikácia bude dostupná na:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

### Knihy

- **GET `/books`**  
  Vráti zoznam všetkých kníh.  
  Podporuje vyhľadávanie (`q`), filtrovanie (`genre`, `author`) a stránkovanie (`limit`, `offset`).

- **GET `/books/{id}`**  
  Vráti detail knihy podľa ID.

- **POST `/books`**  
  Vytvorí novú knihu.  
  Príklad tela požiadavky:
  ```json
  {
    "title": "Názov",
    "author": "Autor",
    "year": 2024,
    "genre": "Žáner",
    "cover_url": "http://..."
  }
  ```

- **PUT `/books/{id}`**  
  Upraví existujúcu knihu.

- **DELETE `/books/{id}`**  
  Odstráni knihu.

- **POST `/books/upload-cover/`**  
  Nahrá obálku knihy (`multipart/form-data`, parametre: `book_id`, `file`).  
  Uloží obrázok do priečinka `covers` a aktualizuje cestu v databáze.

---

## Dokumentácia

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

---

## Požiadavky

- Python 3.11+

---

## Upload obálky knihy

- **Endpoint:** `POST /books/upload-cover/`
- **Parametre:**
  - `book_id` (int, ako query parameter)
  - `file` (obrázok, multipart/form-data)

**Príklad použitia v Postman/Swagger:**
- Zvoľte typ požiadavky `form-data`
- Pole `book_id` nastavte na ID knihy
- Pole `file` – vyberte obrázok

Obrázky sa ukladajú do priečinka `covers/` a cesta sa uloží do poľa `cover_url` v databáze.  
Prístup k obrázku je cez lokálnu cestu (napr. `covers/3_nazov.jpg`).

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

**Spustenie testov:**
```bash
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

- Dáta sú uložené v súbore `books.db` (SQLite).
- Obálky kníh sa ukladajú do priečinka `covers/`.
- API automaticky generuje OpenAPI dokumentáciu.
```

