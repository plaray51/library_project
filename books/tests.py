import pytest
from django.urls import reverse
from .models import Book

# Fixture for creating a book
@pytest.fixture
def book(db):
    return Book.objects.create(
        title="Test Book", 
        author="Author", 
        isbn="1234567890123", 
        published_date="2024-01-01"
    )
    
# Test for creating a book (POST)
@pytest.mark.django_db
def test_create_book(client):
    books_before = Book.objects.count()
    response = client.post(reverse('book-list'), {
        'title': "Another Test Book",
        'author': "Another Author",
        'isbn': "1234567890124",
        'published_date': "2025-01-01"
    })
    books_after = Book.objects.count()
    assert response.status_code == 201
    assert books_after == books_before + 1

# Test for retrieving a book's detail (GET)
@pytest.mark.django_db
def test_book_detail_view(client, book):
    url = reverse('book-detail', args=[book.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['title'] == book.title

# Test for updating a book's detail (PUT)
@pytest.mark.django_db
def test_update_book(client, book):
    url = reverse('book-detail', args=[book.id])
    response = client.put(url, {
        'title': "Updated Test Book",
        'author': "Updated Author",
        'isbn': "1234567890123",
        'published_date': "2026-01-01"
    }, content_type='application/json')
    book.refresh_from_db()
    assert response.status_code == 200
    assert book.title == "Updated Test Book"

# Test for partially updating a book's detail (PATCH)
@pytest.mark.django_db
def test_partial_update_book(client, book):
    url = reverse('book-detail', args=[book.id])
    response = client.patch(url, {
        'title': "Partially Updated Test Book",
    }, content_type='application/json')
    book.refresh_from_db()
    assert response.status_code == 200
    assert book.title == "Partially Updated Test Book"

# Test for deleting a book (DELETE)
@pytest.mark.django_db
def test_delete_book(client, book):
    books_before = Book.objects.count()
    url = reverse('book-detail', args=[book.id])
    response = client.delete(url)
    books_after = Book.objects.count()
    assert response.status_code == 204
    assert books_after == books_before - 1