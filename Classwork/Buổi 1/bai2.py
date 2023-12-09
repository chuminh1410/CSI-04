class Book:
    def __init__(self, name, author, year, page):
        self.name = name
        self.author = author
        self.year = year
        self.page = page

    def new_or_not(self):
        if self.year > 2020:
            print("This is a new book")
        else:
            print("This is an old book")
            
    def show_information(self):
        print(f"Book name is: {self.name}, author is {self.author}, the year published: {self.year}, number of pages: {self.page}")

my_book = Book(name="Sample", author="ABCDE", year=2021, page=300)

print(my_book.year)

my_book.new_or_not()
my_book.show_information()