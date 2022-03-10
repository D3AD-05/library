from django.urls import path
from .views import home, addbook,get_books,book_details,remove_book,update_book

urlpatterns = [
    path('', home, name='home'),
    path('aadbook/', addbook, name='addbook'),
    path("getbooks", get_books, name="search"),
    path("books/<int:id>",book_details,name="details"),
    path("books/remove/<int:id>", remove_book, name="remove"),
    path("books/change/<int:id>", update_book, name="change"),

]
