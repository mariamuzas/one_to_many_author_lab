from db.run_sql import run_sql
from models.author import Author
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, genre) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book