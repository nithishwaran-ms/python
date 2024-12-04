class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"Book '{book}' has been borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"Book '{book}' has been returned.")
        else:
            print(f"Book '{book}' was not borrowed.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Example usage
member1 = Member("Alice", "M001")
member1.borrow_book("The Catcher in the Rye")
member1.borrow_book("To Kill a Mockingbird")
member1.display_borrowed_books()
member1.return_book("The Catcher in the Rye")
member1.display_borrowed_books()

