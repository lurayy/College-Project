from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search', views.search, name = 'search book by name'),
    path('book/register',views.register_book, name = "register new book"),
    path('<str:uuid>',views.book_info, name = "show book info"),
    path('book/assign',views.assign_book, name = "Assign Books"),
    path('book/return',views.book_returned, name = "Return Book"),
    path('book/extend',views.extend_due_date, name = "Extend Due date"),
    
    path('get/sem',views.get_semester, name = "get list of semester"),
    path('get/book',views.get_books, name = "get books according to semester"),
]
