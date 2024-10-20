from django.urls import path
from django.shortcuts import render
from books.views import MyView , BookListView , ContactFormView

urlpatterns = [
    path('initial/', MyView.as_view()),
    path('list/', BookListView.as_view()),
    path('contact/add',ContactFormView.as_view()),
    path('contact_success/', lambda request:render(request, "success/contact_success.html"), name="contact_success")
]