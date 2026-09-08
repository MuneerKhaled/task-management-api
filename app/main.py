from datetime import datetime, timedelta


# =========================================================
# Book Model
# =========================================================

class Book:

    def __init__(self, book_id, title, author, category):
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True
        self.borrowed_by = None
        self.borrowed_at = None
        self.due_date = None
        self.added_at = datetime.now()

    def borrow_book(self, member):

        if not self.available:
            print("\nBook is already borrowed.")
            return False

        self.available = False
        self.borrowed_by = member
        self.borrowed_at = datetime.now()

        # Borrow period = 14 days
        self.due_date = datetime.now() + timedelta(days=14)

        return True

    def return_book(self):

        if self.available:
            print("\nBook is already available.")
            return False

        fine = self.calculate_fine()

        self.available = True
        self.borrowed_by = None
        self.borrowed_at = None
        self.due_date = None

        return fine

    def calculate_fine(self):

        if self.due_date is None:
            return 0

        today = datetime.now()

        if today <= self.due_date:
            return 0

        overdue_days = (today - self.due_date).days

        # Fine = ₹5 per overdue day
        return overdue_days * 5

    def update_book(self, title=None, author=None, category=None):

        if title:
            self.title = title

        if author:
            self.author = author

        if category:
            self.category = category

    def display(self):

        status = "Available" if self.available else "Borrowed"

        print("\n--------------------------------")
        print(f"Book ID     : {self.id}")
        print(f"Title       : {self.title}")
        print(f"Author      : {self.author}")
        print(f"Category    : {self.category}")
        print(f"Status      : {status}")

        if not self.available:
            print(f"Borrowed By : {self.borrowed_by.name}")
            print(f"Due Date    : {self.due_date}")

        print(f"Added       : {self.added_at}")
        print("--------------------------------")


# =========================================================
# Member Model
# =========================================================

class Member:

    def __init__(self, member_id, name, email):

        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
        self.joined_at = datetime.now()

    def borrow_book(self, book):

        if len(self.borrowed_books) >= 3:
            print("\nMember cannot borrow more than 3 books.")
            return False

        self.borrowed_books.append(book)

        return True

    def return_book(self, book):

        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True

        return False

    def display(self):

        print("\n--------------------------------")
        print(f"Member ID       : {self.id}")
        print(f"Name            : {self.name}")
        print(f"Email           : {self.email}")
        print(f"Books Borrowed  : {len(self.borrowed_books)}")
        print(f"Joined At       : {self.joined_at}")
        print("--------------------------------")


# =========================================================
# Library Manager
# =========================================================

class LibraryManager:

    def __init__(self):

        self.books = []
        self.members = []

        self.next_book_id = 1
        self.next_member_id = 1

    # =====================================================
    # BOOK MANAGEMENT
    # =====================================================

    def add_book(self, title, author, category):

        book = Book(
            self.next_book_id,
            title,
            author,
            category
        )

        self.books.append(book)
        self.next_book_id += 1

        print("\nBook added successfully!")

        return book

    def get_book(self, book_id):

        for book in self.books:

            if book.id == book_id:
                return book

        return None

    def get_all_books(self):

        if not self.books:
            print("\nNo books found.")
            return

        print("\n========== ALL BOOKS ==========")

        for book in self.books:
            book.display()

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

        print("\nBook updated successfully!")

    def delete_book(self, book_id):

        book = self.get_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        if not book.available:
            print("\nCannot delete a borrowed book.")
            return

        self.books.remove(book)

        print("\nBook deleted successfully!")

    # =====================================================
    # MEMBER MANAGEMENT
    # =====================================================

    def add_member(self, name, email):

        member = Member(
            self.next_member_id,
            name,
            email
        )

        self.members.append(member)
        self.next_member_id += 1

        print("\nMember added successfully!")

        return member

    def get_member(self, member_id):

        for member in self.members:

            if member.id == member_id:
                return member

        return None

    def get_all_members(self):

        if not self.members:
            print("\nNo members found.")
            return

        print("\n========== ALL MEMBERS ==========")

        for member in self.members:
            member.display()

    # =====================================================
    # BORROW BOOK
    # =====================================================

    def borrow_book(self, book_id, member_id):

        book = self.get_book(book_id)
        member = self.get_member(member_id)

        if book is None:
            print("\nBook not found.")
            return

        if member is None:
            print("\nMember not found.")
            return

        if not book.available:
            print("\nBook is already borrowed.")
            return

        if not member.borrow_book(book):
            return

        book.borrow_book(member)

        print("\nBook borrowed successfully!")

        print(f"Book       : {book.title}")
        print(f"Member     : {member.name}")
        print(f"Due Date   : {book.due_date}")

    # =====================================================
    # RETURN BOOK
    # =====================================================

    def return_book(self, book_id):

        book = self.get_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        if book.available:
            print("\nBook is already available.")
            return

        member = book.borrowed_by

        fine = book.return_book()

        member.return_book(book)

        print("\nBook returned successfully!")

        if fine > 0:
            print(f"Late Fine: ₹{fine}")
        else:
            print("No fine.")

    # =====================================================
    # SEARCH
    # =====================================================

    def search_books(self, keyword):

        results = []

        keyword = keyword.lower()

        for book in self.books:

            if (
                keyword in book.title.lower()
                or keyword in book.author.lower()
                or keyword in book.category.lower()
            ):
                results.append(book)

        if not results:
            print("\nNo matching books found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for book in results:
            book.display()

    # =====================================================
    # AVAILABLE BOOKS
    # =====================================================

    def get_available_books(self):

        available_books = [
            book for book in self.books
            if book.available
        ]

        if not available_books:
            print("\nNo available books.")
            return

        print("\n========== AVAILABLE BOOKS ==========")

        for book in available_books:
            book.display()

    # =====================================================
    # BORROWED BOOKS
    # =====================================================

    def get_borrowed_books(self):

        borrowed_books = [
            book for book in self.books
            if not book.available
        ]

        if not borrowed_books:
            print("\nNo borrowed books.")
            return

        print("\n========== BORROWED BOOKS ==========")

        for book in borrowed_books:
            book.display()

    # =====================================================
    # STATISTICS
    # =====================================================

    def show_statistics(self):

        total_books = len(self.books)

        available_books = len([
            book for book in self.books
            if book.available
        ])

        borrowed_books = total_books - available_books

        total_members = len(self.members)

        print("\n========== LIBRARY STATISTICS ==========")

        print(f"Total Books       : {total_books}")
        print(f"Available Books   : {available_books}")
        print(f"Borrowed Books    : {borrowed_books}")
        print(f"Total Members     : {total_members}")


# =========================================================
# Menu
# =========================================================

def show_menu():

    print("\n")
    print("==========================================")
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("==========================================")

    print("\nBOOK MANAGEMENT")
    print("1. Add book")
    print("2. Show all books")
    print("3. Update book")
    print("4. Delete book")
    print("5. Search books")
    print("6. Show available books")
    print("7. Show borrowed books")

    print("\nMEMBER MANAGEMENT")
    print("8. Add member")
    print("9. Show all members")

    print("\nLIBRARY OPERATIONS")
    print("10. Borrow book")
    print("11. Return book")
    print("12. Show statistics")

    print("13. Exit")

    print("==========================================")


# =========================================================
# Main Application
# =========================================================

def main():

    library = LibraryManager()

    # -----------------------------------------------------
    # Sample Books
    # -----------------------------------------------------

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

    library.add_book(
        "Introduction to Algorithms",
        "Thomas H. Cormen",
        "Algorithms"
    )

    # -----------------------------------------------------
    # Sample Members
    # -----------------------------------------------------

    library.add_member(
        "Muneer",
        "muneer@example.com"
    )

    library.add_member(
        "Rahul",
        "rahul@example.com"
    )

    # -----------------------------------------------------
    # Application Loop
    # -----------------------------------------------------

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        # -------------------------------------------------
        # Add Book
        # -------------------------------------------------

        if choice == "1":

            title = input("Enter book title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")

            library.add_book(
                title,
                author,
                category
            )

        # -------------------------------------------------
        # Show Books
        # -------------------------------------------------

        elif choice == "2":

            library.get_all_books()

        # -------------------------------------------------
        # Update Book
        # -------------------------------------------------

        elif choice == "3":

            try:
                book_id = int(
                    input("Enter book ID: ")
                )

                title = input("Enter new title: ")
                author = input("Enter new author: ")
                category = input("Enter new category: ")

                library.update_book(
                    book_id,
                    title,
                    author,
                    category
                )

            except ValueError:

                print("\nPlease enter a valid book ID.")

        # -------------------------------------------------
        # Delete Book
        # -------------------------------------------------

        elif choice == "4":

            try:

                book_id = int(
                    input("Enter book ID: ")
                )

                library.delete_book(book_id)

            except ValueError:

                print("\nPlease enter a valid book ID.")

        # -------------------------------------------------
        # Search
        # -------------------------------------------------

        elif choice == "5":

            keyword = input(
                "Enter title, author or category: "
            )

            library.search_books(keyword)

        # -------------------------------------------------
        # Available Books
        # -------------------------------------------------

        elif choice == "6":

            library.get_available_books()

        # -------------------------------------------------
        # Borrowed Books
        # -------------------------------------------------

        elif choice == "7":

            library.get_borrowed_books()

        # -------------------------------------------------
        # Add Member
        # -------------------------------------------------

        elif choice == "8":

            name = input("Enter member name: ")
            email = input("Enter member email: ")

            library.add_member(
                name,
                email
            )

        # -------------------------------------------------
        # Show Members
        # -------------------------------------------------

        elif choice == "9":

            library.get_all_members()

        # -------------------------------------------------
        # Borrow Book
        # -------------------------------------------------

        elif choice == "10":

            try:

                book_id = int(
                    input("Enter book ID: ")
                )

                member_id = int(
                    input("Enter member ID: ")
                )

                library.borrow_book(
                    book_id,
                    member_id
                )

            except ValueError:

                print("\nPlease enter valid IDs.")

        # -------------------------------------------------
        # Return Book
        # -------------------------------------------------

        elif choice == "11":

            try:

                book_id = int(
                    input("Enter book ID: ")
                )

                library.return_book(book_id)

            except ValueError:

                print("\nPlease enter a valid book ID.")

        # -------------------------------------------------
        # Statistics
        # -------------------------------------------------

        elif choice == "12":

            library.show_statistics()

        # -------------------------------------------------
        # Exit
        # -------------------------------------------------

        elif choice == "13":

            print(
                "\nThank you for using "
                "the Library Management System!"
            )

            break

        # -------------------------------------------------
        # Invalid Choice
        # -------------------------------------------------

        else:

            print(
                "\nInvalid choice. "
                "Please select a valid option."
            )


# =========================================================
# Start Application
# =========================================================

if __name__ == "__main__":
    main()