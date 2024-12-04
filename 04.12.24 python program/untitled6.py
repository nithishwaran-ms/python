class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        """Adds a new book to the library."""
        if title in self.books:
            print(f"Book '{title}' is already in the library.")
        else:
            self.books[title] = True  # True indicates the book is available
            print(f"Book '{title}' has been added to the library.")

    def borrow_book(self, title):
        """Marks a book as borrowed if it’s available."""
        if title in self.books:
            if self.books[title]:
                self.books[title] = False  # False indicates the book is borrowed
                print(f"Book '{title}' has been borrowed.")
            else:
                print(f"Book '{title}' is currently borrowed.")
        else:
            print(f"Book '{title}' is not available in the library.")

    def return_book(self, title):
        """Marks a book as available."""
        if title in self.books:
            if not self.books[title]:
                self.books[title] = True  # Mark the book as available
                print(f"Book '{title}' has been returned.")
            else:
                print(f"Book '{title}' was not borrowed.")
        else:
            print(f"Book '{title}' is not available in the library.")

    def view_books(self):
        """Displays the list of all books and their availability status."""
        if not self.books:
            print("No books are available in the library.")
        else:
            for title, is_available in self.books.items():
                status = "Available" if is_available else "Borrowed"
                print(f"'{title}': {status}")

# Example Task: Demonstrating the Library class
def library_management_task():
    # Create a new library
    library = Library()
    
    # Add books to the library
    library.add_book("1984 by George Orwell")
    library.add_book("To Kill a Mockingbird by Harper Lee")
    library.add_book("The Great Gatsby by F. Scott Fitzgerald")
    
    # View all books in the library
    library.view_books()
    
    # Borrow a book
    library.borrow_book("1984 by George Orwell")
    
    # Try to borrow the same book again
    library.borrow_book("1984 by George Orwell")
    
    # Return the book
    library.return_book("1984 by George Orwell")
    
    # View all books in the library again
    library.view_books()

# Execute the task
library_management_task()