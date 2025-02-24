class Library:
    def __init__(self):
        self.books = {}  # Stores book titles and availability

    def add_book(self, title):
        self.books[title] = "Available"

    def lend_book(self, title, user):
        if self.books.get(title) == "Available":
            self.books[title] = f"Lent to {user}"
        else:
            print("Book not available.")

    def return_book(self, title):
        if "Lent to" in self.books.get(title, ""):
            self.books[title] = "Available"

    def display_books(self):
        for title, status in self.books.items():
            print(f"{title}: {status}")


# Usage
library = Library()
num = int(input("Enter the number of books to add: "))
for i in range(num):
    book = input(f"Enter the title of book {i+1}: ")
library.add_book(book)

library.display_books()

library.lend_book("Python Programming", "Alice")
library.display_books()

library.return_book("Python Programming")
library.display_books()
