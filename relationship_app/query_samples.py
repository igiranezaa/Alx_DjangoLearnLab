from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.first()
books_by_author = Book.objects.filter(author=author)
print('Books by author:', books_by_author)

library = Library.objects.first()
all_books = library.books.all()
print('Books in library:', all_books)

librarian = Librarian.objects.get(library=library)
print('Librarian:', librarian)
