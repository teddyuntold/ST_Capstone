from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.id
    


class Checkout(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"