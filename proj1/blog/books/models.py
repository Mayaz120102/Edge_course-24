from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    website = models.URLField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True ,blank=True)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)