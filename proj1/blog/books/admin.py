from django.contrib import admin

# Register your models here.
from books.models import Author, Book, Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ist_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
