from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView , FormView ,CreateView
from django.urls import reverse_lazy
from books.models import Book
from books.forms import ContactForm , BookForm





class MyView(View):
    def get(self,request):
        return HttpResponse("welcome to django!")


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class ContactFormView(FormView):
    template_name = 'contact.html'  
    form_class = ContactForm        
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):

        return super().form_valid(form)
    

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_success')
