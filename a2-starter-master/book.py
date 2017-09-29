# create your simple Book class in this file
class Book:
    __title = ""
    __author = ""
    __page = 0
    __status = 'r'

    def __init__(self, t, a, p, s):
        """
        construct method
        :param t: title
        :param a: author
        :param p: page
        :param s: status
        """
        self.__title = t
        self.__author = a
        self.__page = p
        self.__status = s

    def __str__(self):
        """
        showing details of book in a string
        :return: string to display the details of the book
        """
        printStr = self.__title + " by " + self.__author + ", " + self.__page + " pages ("

        if self.__status == 'r':
            printStr += 'Required'
        else:
            printStr += 'Completed'
        printStr += ')'
        return printStr

    def getTitle(self):
        """
        get title
        :return: title
        """
        return self.__title

    def getAuthor(self):
        """
        get author
        :return: author
        """
        return self.__author

    def getStatus(self):
        """
        get status
        :return: status
        """
        return self.__status

    def getPage(self):
        """
        get page
        :return: page
        """
        return self.__page

    def markComplete(self):
        """
        mark the status of this book as 'c'
        :return: NA
        """
        self.__status = 'c'

    def isLong(self):
        """
        tell whether the book is long or not (>500)
        :return: true if page is larger than 500, otherwise false
        """
        if int(self.__page) > 500:
            return True
        else:
            return False

    def isBefore(self, compare):
        """
        compare to another book
        :param compare: compared book
        :return: true if this book should be in front of compare, otherwise false
        """
        if compare.__author < self.__author:
            return False
        elif self.__author == compare.__author and self.__page > compare.__page:
            return False
        else:
            return True