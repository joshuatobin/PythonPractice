
class Library:
    """
    Create a Library class with attributes for a list of books, library name, and location.
    
    Add methods to the Library class for:
    * Adding a new book.
    * Checking out a book (change its status to unavailable).
    * Returning a book (change its status to available).

    Use inheritance to create subclasses for specialized book types, such as EBook and PrintedBook, each with unique attributes (e.g., file format for EBook and physical condition for PrintedBook).
    """

    def __init__(self, books, name: str, location: str):
        """Initializes the library with a list of books, name, and location."""
        # Ensure self.books is always a list.
        self.books = books if books else []
        self.name = name
        self.location = location
    
    def add_book(self, book):
        """Adds a Book instance to the library's collection."""
        self.books.append(book)
    
        return book
    
    def checkout(self, title):
        """ Adds a checkout of a Book instance"""

        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"'{book.title}' has been checked out.")
            else:
                print(f"'{book.title}' is not available or does not exist.")

    def book_return(self, title):
        """ Returning a book (change its status to available)"""

        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"'{book.title}' has been checked back in.")
            else:
                print(f"'{book.title}' cannot be checked in.")

class Book:
    def __init__(self, title: str, author: str, available: bool):
        """Initializes a Book with title, author, and availability status."""
        self.title = title
        self.author = author
        self.available = True

class Ebook(Book):
    def __init__(self, title, author, available, file_format, file_size):
        super().__init__(title, author, available)
        self.file_format = file_format
        self.file_size = file_size  # In megabytes
    
    def download(self):
        print(f"Downloading {self.title} ({self.file_size}MB, {self.file_format}).")

def main():

    # Create a book instance.
    moby_dick = Book("Moby Dick", "Herman Melville", True)

    # Initialize the library with an empty list of books.
    library = Library([], "SF Library", "SF")

    # Add the book to the library.
    library.add_book(moby_dick) 

    # Check out the Moby Dick title
    library.checkout("Moby Dick")

    # Check out a non existing title
    library.checkout("Moby Foo")

    library.book_return("Moby Dick")

    # Create an EBook instance
    ebook = Ebook("Digital Transformation", "Jane Doe", True, "EPUB", 5)

    # Download the EBook
    ebook.download()

if __name__ == "__main__":
    main()
