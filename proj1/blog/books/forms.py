from django import forms
from django.core.exceptions import ValidationError
from books.models import Book

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise ValidationError("Email must be from example.com domain. ")
        
        return email
    

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'published_date', 'price', 'author', 'publisher']
 
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price<= 0:
            raise forms.ValidationError("the price must be positive !")
        
        return price
