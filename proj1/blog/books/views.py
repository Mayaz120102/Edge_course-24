from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView , FormView ,CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator



#from rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.forms import ContactForm , BookForm
from .serializers import BookSerializer

@method_decorator(permission_required('books.can_view_sensitive_data', raise_exception=True), name='dispatch')

class SensitiveBookDataView(View):
    template_name = 'sensitive_book_data.html'

    
    def get(self, request):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})

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

#Restframework APIs

class BookListCreateView(APIView):
    def get(self, request):
        books  = Book.objects.all()
        serializer  = BookSerializer(books, many = True)
        data = serializer.data
        return Response(data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
          