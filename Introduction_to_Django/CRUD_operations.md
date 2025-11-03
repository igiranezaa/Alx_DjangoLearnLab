# CRUD_operations.md

## Create
>>> from bookshelf.models import Book
>>> b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> b
<Book: 1984 by George Orwell (1949)>

## Retrieve
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

## Update
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

## Delete
>>> b.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
