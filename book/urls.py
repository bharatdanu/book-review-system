from django.urls import path
from .views import book_create,book_list,book_detail,update_detail,delete_book

urlpatterns = [
    path("book/new/",book_create,name="book-create"),
    path("",book_list,name="book-list"),
    path("book/<int:bk_id>",book_detail,name="book-detail"),
    path("book/<int:bk_id>/edit/",update_detail,name="update-detail"),
    path("book/<int:bk_id>/delete/",delete_book,name="delete-book"),
]