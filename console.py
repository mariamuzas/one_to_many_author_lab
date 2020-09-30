import pdb
from models.author import Author
from models.book import Book 
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author('Roald Dahl')
author_repository.save(author_1)
author_2 = Author('Fyodor Dostoevsky')
author_repository.save(author_2)

author_repository.select_all()


book_1 = Book('BFG', 'children')
book_repository.save(book_1)
book_2 = Book('Crime and Punishment', 'drama')
book_repository.save(book_2)

book_repository.select_all()

pdb.set_trace()