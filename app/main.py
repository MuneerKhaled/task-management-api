from datetime import datetime


# =========================
# Book Model
# =========================

class Book:
    def __init__(self, book_id, title, author, category):
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True
        self.added_at = datetime.now()

    def borrow_book(self):
        if not self.available:
            print("\nBook is already borrowed.")
            return False

        self.available = False
        return True

    def return_book(self):
        if self.available:
            print("\nBook is already available.")
            return False

        self.available = True
        return True

    def update_book(self, title=None, author=None, category=None):
        if title:
            self.title = title

        if author:
            self.author = author

        if category:
            self.category = category

    def display(self):
        status = "Available" if self.available else "Borrowed"

        print(f"\nBook ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")
        print(f"Status: {status}")
        print(f"Added: {self.added_at}")


# =========================
# Library Manager
# =========================

class LibraryManager:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author, category):
        book = Book(
            self.next_id,
            title,
            author,
            category
        )

        self.books.append(book)
        self.next_id += 1

        print("\nBook added successfully!")
        return book

    def get_all_books(self):
        if not self.books:
            print("\nNo books found.")
            return

        print("\n========== ALL BOOKS ==========")

        for book in self.books:
            book.display()

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book

        return None

    def borrow_book(self, book_id):
        book = self.get_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        if book.borrow_book():
            print(f"\nBook {book_id} borrowed successfully!")

    def return_book(self, book_id):
        book = self.get_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        if book.return_book():
            print(f"\nBook {book_id} returned successfully!")

    def update_book(
        self,
        book_id,
        title=None,
        author=None,
        category=None
    ):
        book = self.get_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        book.update_book(
            title,
            author,
            category
        )

        print(f"\nBook {book_id} updated successfully!")

    def delete_book(self, book_id):
        book = self.get_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        self.books.remove(book)

        print(f"\nBook {book_id} deleted successfully!")

    def search_books(self, keyword):
        results = []

        for book in self.books:
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword.lower() in book.category.lower()
            ):
                results.append(book)

        if not results:
            print("\nNo matching books found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for book in results:
            book.display()

    def get_available_books(self):
        available = [
            book for book in self.books
            if book.available
        ]

        if not available:
            print("\nNo available books.")
            return

        print("\n========== AVAILABLE BOOKS ==========")

        for book in available:
            book.display()

    def get_borrowed_books(self):
        borrowed = [
            book for book in self.books
            if not book.available
        ]

        if not borrowed:
            print("\nNo borrowed books.")
            return

        print("\n========== BORROWED BOOKS ==========")

        for book in borrowed:
            book.display()


# =========================
# Application Menu
# =========================

def show_menu():
    print("\n")
    print("================================")
    print("      LIBRARY MANAGEMENT APP")
    print("================================")
    print("1. Add book")
    print("2. Show all books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Update book")
    print("6. Delete book")
    print("7. Search books")
    print("8. Show available books")
    print("9. Show borrowed books")
    print("10. Exit")
    print("================================")


# =========================
# Main Application
# =========================

def main():

    library = LibraryManager()

    # Example books

    library.add_book(
        "Python Crash Course",
        "Eric Matthes",
        "Programming"
    )

    library.add_book(
        "Clean Code",
        "Robert C. Martin",
        "Software Engineering"
    )

    library.add_book(
        "The Pragmatic Programmer",
        "Andrew Hunt",
        "Programming"
    )

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        # Add book
        if choice == "1":

            title = input("Enter book title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")

            library.add_book(
                title,
                author,
                category
            )

        # Show all books
        elif choice == "2":

            library.get_all_books()

        # Borrow book
        elif choice == "3":

            book_id = int(
                input("Enter book ID: ")
            )

            library.borrow_book(book_id)

        # Return book
        elif choice == "4":

            book_id = int(
                input("Enter book ID: ")
            )

            library.return_book(book_id)

        # Update book
        elif choice == "5":

            book_id = int(
                input("Enter book ID: ")
            )

            title = input(
                "Enter new title: "
            )

            author = input(
                "Enter new author: "
            )

            category = input(
                "Enter new category: "
            )

            library.update_book(
                book_id,
                title,
                author,
                category
            )

        # Delete book
        elif choice == "6":

            book_id = int(
                input("Enter book ID: ")
            )

            library.delete_book(book_id)

        # Search books
        elif choice == "7":

            keyword = input(
                "Enter search keyword: "
            )

            library.search_books(keyword)

        # Available books
        elif choice == "8":

            library.get_available_books()

        # Borrowed books
        elif choice == "9":

            library.get_borrowed_books()

        # Exit
        elif choice == "10":

            print("\nThank you for using the Library Management App!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# =========================
# Start Application
# =========================

if __name__ == "__main__":
    main()