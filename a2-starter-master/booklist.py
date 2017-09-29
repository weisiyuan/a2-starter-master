# create your BookList class in this file
import csv

from book import Book
class BookList:
    __books = []

    def __init__(self):
         __books = []

    #return books
    def getBooks(self):
        return self.__books

    #load books into __books from books.csv
    def loadBook(self):
        with open('books.csv') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                self.__books.append(Book(row[0], row[1], row[2], row[3]))
        print (str(len(self.__books)) + " books load from books.csv")

    #saving __books into books.csv
    def saveBook(self):
        with open('books.csv', 'w') as f:
            f_csv = csv.writer(f)
            for book in self.__books:
                f_csv.writerow([book.getTitle(), book.getAuthor(), book.getPage(), book.getStatus()])

    #add a book based on string information
    def addBook(self, title, author, page):
        self.__books.append(Book(title, author, page, 'r'))

    #add a book entity
    def addBook2(self, book):
        self.__books.append(book)

    #search __book based on title
    def getBookByTitle(self, t):
        """
        search through __book to find the book with title = t
        :param t: title of wanted book
        :return: the wanted book or None
        """
        for book in self.__books:
            if book.getTitle() == t:
                return book
        return None


    def getTotalPage(self):
        """
        get the total pages of all books in __books
        :return: number of pages of all books
        """
        total = 0
        for book in self.__books:
            total += int(book.getPage())
        return total

    def sort(self):
        """
        sorting the books based on author and number of pages
        :return: NA
        """
        iter_len = len(self.__books)
        for i in range(1, iter_len):
            key = self.__books[i]
            j = i - 1
            while j >= 0 and key.isBefore(self.__books[j]):
                self.__books[j + 1] = self.__books[j]
                j -= 1
            self.__books[j + 1] = key




