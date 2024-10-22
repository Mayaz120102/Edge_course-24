from django.urls import path
from django.shortcuts import render
from books.views import MyView , BookListView , ContactFormView , BookCreateView

urlpatterns = [
    path('initial/', MyView.as_view(), name='initial'),
    path('list/', BookListView.as_view(), name= 'book_list'),
    path('contact/add',ContactFormView.as_view(), name='contact_form'),
    path('contact_success/', lambda request:render(request, "success/contact_success.html"), name="contact_success"),
    path('add-book/', BookCreateView.as_view(), name='add_book'),
    path('books_success/', lambda request:render(request, "success/book_success.html"), name="book_success"),
]