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

def select_all():
    book_list = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)
    
    for row in results:
        book = Book(row['title'], row['genre'], row['id'])
        book_list.append(book)
    return book_list