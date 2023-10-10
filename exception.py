#Imagine you are building a text editor application. Write a Python program that takes user input
#for a new document('s content and allows the user to save it to a file. '
#However, if the user tries to save the document with an empty title or if the file already exists, raise custom exceptions and handle them gracefully.

# try:
#     file_name = input("Enter a file name: ")
#     file = open(file_name, 'w')
#     content = input("enter a content of a file : ")
#     file.write(content)
#     file.close()
#     print("File saved successfully!:)")
# class EmptyTitleError(Exception):
#     pass
#
# class FileExistsError(Exception):
#     pass
#
# def save_to_file(file_name,content):
#     try:
#         if not file_name:
#             raise ValueError("Error: File name cannot be empty.")
#
#         # Try to create the file
#         with open(file_name, 'x') as file:
#             file.write(content)
#         print("File saved successfully!")
#     except FileExistsError:
#         print(f"Error: The file '{file_name}' already exists Choose a different name.")
#     except ValueError as ve:
#         print(ve)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# def main():
#     try:
#         file_name = input("Enter the desired file name: ")
#
#         content = input("Enter the content to be written to the file: ")
#
#         save_to_file(file_name, content)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     main()

# def save_to_file(file_name, content):
#     if not file_name:
#         raise ValueError("Error: File name cannot be empty.")
#
#     if not content:
#         print("Error: Content cannot be empty.")
#         return
#
#     try:
#         with open(file_name, 'x') as file:
#             file.write(content)
#         print("File saved successfully!")
#     except FileExistsError:
#         print(f"FILE ERROR: The file '{file_name}' already exists. Choose a different name.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#
# def main():
#     try:
#         file_name = input("Enter the file name: ")
#         content = input("Write the content: ")
#         save_to_file(file_name, content)
#     except ValueError as ve:
#         print(ve)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     main()


# try:
#     file_name = input("Enter the file name: ")
#     content = input("Write the content: ")
#
#     if not file_name:
#         raise ValueError("Error: File name cannot be empty.")
#
#     if not content:
#         print("Error: Content cannot be empty.")
#     else:
#         with open(file_name, 'x') as file:
#             file.write(content)
#         print("File saved successfully!")
# except FileExistsError:
#     print(f"FILE ERROR: The file '{file_name}' already exists.Choose a different name.")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(f"An error occurred: {e}")
class Book:
    def _init_(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def _str_(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}"

def load_books():
    try:
        with open("library.txt", "r") as file:
            lines = file.readlines()
            books = []
            for i in range(0, len(lines), 3):
                title = lines[i].strip()
                author = lines[i + 1].strip()
                publication_year = int(lines[i + 2].strip())
                book = Book(title, author, publication_year)
                books.append(book)
            return books
    except FileNotFoundError:
        return []

def save_books(books):
    try:
        with open("library.txt", "w") as file:
            for book in books:
                file.write(book.title + "\n")
                file.write(book.author + "\n")
                file.write(str(book.publication_year) + "\n")
    except Exception as e:
        print(f"An error occurred while saving the library: {e}")

def add_book(books, new_book):
    for book in books:
        if book.title == new_book.title:
            raise ValueError("A book with the same title already exists in the library")

    books.append(new_book)
    save_books(books)

def search_book(books, title):
    for book in books:
        if book.title.lower() == title.lower():
            return book
    return None

def main():
    books = load_books()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = input("Enter the publication year of the book: ")

            try:
                publication_year = int(publication_year)
            except ValueError:
                print("Invalid input for publication year. Please enter a valid year.")
                continue

            new_book = Book(title, author, publication_year)

            try:
                add_book(books, new_book)
                print("Book added to the library successfully!")
            except ValueError as ve:
                print(ve)

        elif choice == "2":
            title = input("Enter the title of the book you want to search for: ")
            found_book = search_book(books, title)
            if found_book:
                print("Book found:\n", found_book)
            else:
                print("Book not found in the library.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please select a valid option (1/2/3).")


if_name_ == "_main_":
    main()