class Book:
    """A class representing a book with title, author, and checkout status."""

    def __init__(self, title, author):
        """Initialize the book with title, author, and availability."""
        self.title = title               # Public attribute
        self.author = author             # Public attribute
        self._is_checked_out = False     # Private attribute (conventionally private)

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return f'"{self.title}" has been checked out.'
        return f'"{self.title}" is already checked out.'

    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return f'"{self.title}" has been returned.'
        return f'"{self.title}" was not checked out.'

    def is_available(self):
        """Check whether the book is currently available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)
        return f'"{book.title}" by {book.author} added to the library.'

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    book.check_out()
                    return f'You have checked out "{book.title}".'
                else:
                    return f'"{book.title}" is currently unavailable.'
        return f'Book titled "{title}" not found in the library.'

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    book.return_book()
                    return f'You have returned "{book.title}".'
                else:
                    return f'"{book.title}" was not checked out.'
        return f'Book titled "{title}" not found in the library.'

    def list_available_books(self):
        """Return a list of all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            return "No books are currently available."
        return [f'{book.title} by {book.author}' for book in available_books]
