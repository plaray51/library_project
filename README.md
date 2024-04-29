### Run tests with
pytest

### Run server with
python manage.py runserver

### GET
**Get All Books**
http://127.0.0.1:8000/api/books/

**Retrieve a specific book**
http://127.0.0.1:8000/api/books/{id}/

### POST
**Make A New Book**
http://127.0.0.1:8000/api/books

**Request Body (JSON):**
```json
{
  "title": "New Book 2",
  "author": "Author Name",
  "isbn": "1234567890113",
  "published_date": "2024-01-01"
}
```

### PUT
**Update a book**
http://127.0.0.1:8000/api/books/{id}/

Request Body (JSON):
```json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "isbn": "1234567330123",
  "published_date": "2024-01-01"
}
```

### PATCH
**Partially Update A Book**
http://127.0.0.1:8000/api/books/{id}/

Request Body (JSON):

```json
{
    "title": "Partially Updated"
}
```

### DELETE
**Delete a book**
http://127.0.0.1:8000/api/books/{id}/

