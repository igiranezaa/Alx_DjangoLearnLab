# Retrieve
from bookshelf.models import Book
Book.objects.get(title='1984')
# Expected output: <Book: 1984>
