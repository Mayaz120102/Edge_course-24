from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self) -> str:
        return self.name 

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

    

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True ,blank=True)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    created_ap = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        permissions = [
            ("can_view_sensitive_data", "Can view sensitive book data"),
        ]
     

    def __str__(self):
        return self.title