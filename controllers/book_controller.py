from flask import Flask, render_template
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books= books)
