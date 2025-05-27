class Book:
    total_books = 0  

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment book count when a book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Creating book objects
book1 = Book("Python Programming")
book2 = Book("Data Structures")
book3 = Book("Algorithms")

# Print total number of books
print("Total Books:", Book.get_total_books())
