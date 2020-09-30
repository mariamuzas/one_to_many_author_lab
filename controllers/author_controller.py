from flask import Flask, render_template
from flask import Blueprint
from models.author import Author
import repositories.author_repository as author_repository

author_blueprint = Blueprint("authors", __name__)

@author_blueprint.route("/authors")
def authors():
    authors = author_repository.select_all()
    return render_template("authors/index.html", authors= authors)
