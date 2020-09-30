import pdb
from models.author import Author
from models.book import Book 
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author('Roald Dahl')
author_repository.save(author_1)

book_1 = Book('BFG', 'children')
book_repository.save(book_1)

pdb.set_trace()