import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create Authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

# Create Books
book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
book3 = Book.objects.create(title="1984", author=author2)

# Create Library
library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2, book3)

# Create Librarian
librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)

print("Sample data populated successfully!")
