from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

class Books(models.Model):
    book_title = models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    prize=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.book_title
    

