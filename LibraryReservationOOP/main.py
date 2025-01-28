
import datetime

class Library():
    """
    `Library`: Represents the entire library and maintains a catalog of books.
    """

    def __init__(self, *books):
        self.books = list(books)
        self.reservations = []
        
    def all(self):
        return self.books 
    
    def get_reservations(self):
        return f"{self.reservations}"
    
    def reserve_book(self, title):
        """
        Finds the book.
        Checks if it’s available.
        Creates a new Reservation object and associates it with the book.
        """

         # Find the title
        book = self._search_by_title(title)

        # If available, reserve
        if book.is_available:
            r = Reservation(book, reserved=True)
            self.reservations.append(r)
            book.is_reserved = True
        
        return True        
    
    def cancel_reservation(self, title):
        """
        Cancel a reservation.
        """
        # Find the title
        book = self._search_by_title(title)

        # Check reservations to see if one exists
        reservation = [r for r in self.reservations if r.book == book ]
        
        # If found remove from reservations, and also mark is_reserved = False
        if reservation:
            self.reservations.remove(reservation[0])  # Removes the Reservation instance from the list
            book.is_reserved = False  # Updates the book’s availability status

    def _search_by_title(self, title):
        """
        Private shared method to provide a book by title
        """
        b = self.search(title=title)
        book = b[0] if b else None
        
        return book
    
    def search(self, author=None, title=None):
        """
        Search
        """
        results = self.books

        if title:
            results = [b for b in results if title.lower() in b.title.lower()]
        if author:
            results = [b for b in results if author.lower() in b.author.lower()]

        # *** REMEMBER In Python, if a function has no return statement, it implicitly returns None.      
        return results
        
    def __repr__(self):
        return(f"Library -> all books: {self.all()}")
    
class Book():
    """
    `Book`: Represents a single book in the catalog, including attributes like title, author, and availability status. 
    """
    
    def __init__(self, author, title, is_reserved=False):
        self.is_reserved = is_reserved
        self.author = author
        self.title = title 
        
    def is_available(self):
        """
        Iterate through the catalog and return only available books.  
        """
        
        if self.is_reserved is False:
            return True

    def __repr__(self):
        """
        Return a representation of the Book
        """
        
        return(f"Book: {self.title}, by: {self.author}, reserved: {self.is_reserved}")

class Reservation():
    """
    - `Reservation`: Represents a reservation made by a user for a specific book.  
    
    * Implement the `Reservation` class so that each reservation is linked to a specific `Book`.
    """
    
    def __init__(self, book, reserved=None, cancelled=None, expired=None):
        self.book = book
        self.reserved = reserved
        self.cancelled = cancelled
        self.expired = expired
        self.now = datetime.datetime.now()
    
    def __repr__(self):
        """
        Return a representation of the Reservations
        """
        
        return(f"Reservation: at: {self.now}, by: {self.cancelled}, reserved: {self.expired}")
def main():
    """
    Design a system that allows users to:
    - Search for available books by title or author.  
    - Reserve a book.  
    - Cancel a reservation.
    """
    
    book1 = Book(title="Foo", author="bar", is_reserved=True)
    book2 = Book(title="Moby Dick", author="Hemmingway", is_reserved=False)
    
    library = Library(book1, book2)    

    reserve = library.reserve_book(book2.title)
    cancel = library.cancel_reservation(book2.title)
    
if __name__ == "__main__":
    main()
