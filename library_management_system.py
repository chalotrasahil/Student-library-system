"""
Author: Sahil Chalotra
Project: Book Issue Management System
Description: A simple console-based library management system
"""

class BookManager:
    def __init__(self):
        self.available = [
            "vistas",
            "invention",
            "rich and poor",
            "indian economy",
            "macroeconomics",
            "microeconomics"
        ]
        self.issued = []   # list of dicts → {"student": name, "book": book}

    def show_books(self):
        print("\n📚 AVAILABLE BOOKS:")
        if not self.available:
            print("No books available\n")
            return
        for b in self.available:
            print(" >", b)
        print()

    def issue(self):
        name = input("Student name: ")
        book = input("Book name: ").lower()

        if book not in self.available:
            print("Book not available\n")
            return

        self.available.remove(book)
        self.issued.append({"student": name, "book": book})
        print("Book issued successfully\n")

    def submit(self):
        name = input("Student name: ")
        book = input("Book name: ").lower()

        record = {"student": name, "book": book}
        if record not in self.issued:
            print("No matching record found\n")
            return

        self.issued.remove(record)
        self.available.append(book)
        print("Book returned successfully\n")

    def donate(self):
        book = input("Book name to donate: ").lower()
        self.available.append(book)
        print("Thank you for donating the book!\n")

    def history(self):
        print("\n📖 ISSUED RECORDS:")
        if not self.issued:
            print("None\n")
            return
        for r in self.issued:
            print(f"{r['book']} → {r['student']}")
        print()


manager = BookManager()

while True:
    print("""
========= LIBRARY MENU =========
1. Show books
2. Issue book
3. Return book
4. Donate book
5. Issued history
6. Exit
===============================
""")

    ch = input("Choice: ")

    if ch == "1":
        manager.show_books()

    elif ch == "2":
        manager.issue()

    elif ch == "3":
        manager.submit()

    elif ch == "4":
        manager.donate()

    elif ch == "5":
        manager.history()

    elif ch == "6":
        print("Thank you for using the library system!")
        break

    else:
        print("Invalid choice\n")
