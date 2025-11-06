from django.contrib import admin
from django.urls import path
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list_books'),
    path('authors/', views.list_authors, name='list_authors'),
    path('libraries/', views.list_libraries, name='list_libraries'),
    path('librarians/', views.list_librarians, name='list_librarians'),
]
