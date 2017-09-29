"""
(incomplete) Tests for Book class
"""
from book import Book
from booklist import BookList

# test initial-value book
book2 = Book("Fish fingers", "Dory", 2, 'r')

list = BookList()
list.loadBook()
list.saveBook()
