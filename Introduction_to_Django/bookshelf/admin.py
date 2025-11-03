from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')                     # add search box
    list_filter = ('publication_year',)                     # add filter by year

admin.site.register(Book, BookAdmin)
