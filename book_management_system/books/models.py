from django.db import models

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