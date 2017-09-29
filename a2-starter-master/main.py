"""
Name: Wei Siyuan
Date: 2017-01-29
Brief Project Description: a reading list to help users to keep tracking of reading history
GitHub URL: https://github.com/ParisWei/a2-starter-master.git
"""
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import BookList

# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    """
    Main app to show readling list
    """
    LONG_BOOK_COLOR = [0.2,0.7,0.9,1]
    SHORT_BOOK_COLOR = [0.9,0.7,0.2,1]
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.list = BookList()
        self.list.loadBook()


    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_book_buttons('r')
        return self.root

    def create_book_buttons(self, s):
        """
        Refresh the list of book on right side
        :param s: the book status, can be 'r' or 'c'
        :return: NA
        """
        self.root.ids.listview.clear_widgets()
        total = 0
        for book in self.list.getBooks():
            if book.getStatus() == s:
                total += int(book.getPage())
                if s == 'r' and book.isLong():
                    temp_button = Button(text=book.getTitle(), background_color=self.LONG_BOOK_COLOR)
                elif s == 'r':
                    temp_button = Button(text=book.getTitle(), background_color=self.SHORT_BOOK_COLOR)
                else:
                    temp_button = Button(text=book.getTitle())
                temp_button.bind(on_release=self.press_entry)
                self.root.ids.listview.add_widget(temp_button)
        header = "Total pages "
        if (s == 'c'):
            header += 'completed'
            self.root.ids.footer_status.text = "Click one book to see details"
        else:
            header += 'to read'
            self.root.ids.footer_status.text = "Click books to mark them as completed"
        header += ': ' + str(total)
        self.root.ids.header_status.text = header


    def press_entry(self, instance):
        """
        react to click on one of book in list, either complete the book or show detail information
        :param instance: the button being pressed
        :return: NA
        """
        name = instance.text
        book = self.list.getBookByTitle(name)
        if(book.getStatus() == 'r'):
            book.markComplete()
            self.press_clear()
            self.create_book_buttons('r')
        else:
            self.root.ids.footer_status.text = book.__str__()
        instance.state = 'down'

    def press_clear(self):
        """
        Clear three input fields on left side
        :return: NA
        """
        self.root.ids.title.text = ''
        self.root.ids.author.text = ''
        self.root.ids.page.text = ''



    def press_add(self):
        """
        Add a required book based on the information filled
        :return: NA
        """
        if (self.getInputString(self.root.ids.title.text)
                and self.getInputString(self.root.ids.author.text)
                and self.getInputInt(self.root.ids.page.text)):
            self.list.addBook(self.root.ids.title.text, self.root.ids.author.text, self.root.ids.page.text)
            self.press_clear()
            self.create_book_buttons('r')

    def on_stop(self):
        """
        save the book list to csv on exit
        :return: NA
        """
        self.list.saveBook()

    # validate string input
    def getInputString(self, inputStr):
        """
        valid whether a string input is empty
        :param inputStr: the string being examined
        :return:
        """
        if (len(inputStr) == 0):
            self.root.ids.footer_status.text = ("All fields must be completed")
            return False
        else:
            return True

    # validate integer input
    def getInputInt(self, intInput):
        """
        check whether input is a valid integer
        :param intInput: the string being examined
        :return:
        """
        emptyCheck = self.getInputString(intInput)
        if emptyCheck == False:
            return False
        try:
            num = int(intInput)
        except ValueError:
            self.root.ids.footer_status.text = ("Please enter a valid number")
            return False
        else:
            if num >= 0:
                return True
            else:
                self.root.ids.footer_status.text = ("Number must be >= 0")
                return False

ReadingListApp().run()



