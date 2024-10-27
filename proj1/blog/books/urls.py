from django.urls import path
from django.shortcuts import render
from books.views import MyView , BookListView , ContactFormView , BookCreateView , SensitiveBookDataView, BookListCreateView

urlpatterns = [
    path('initial/', MyView.as_view(), name='initial'),
    path('list/', BookListView.as_view(), name= 'book_list'),
    path('contact/add',ContactFormView.as_view(), name='contact_form'),
    path('contact_success/', lambda request:render(request, "success/contact_success.html"), name="contact_success"),
    path('add-book/', BookCreateView.as_view(), name='add_book'),
    path('books_success/', lambda request:render(request, "success/book_success.html"), name="book_success"),
    path('sensitive-data/', SensitiveBookDataView.as_view(), name= 'sensitive_date'),
    path('books_rest/', BookListCreateView.as_view(), name= "books_list_create"),
]