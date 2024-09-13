from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    content = models.TextField(unique=True)
    author = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE)
    CATEGORY_CHOICES = (
        ('Li', 'Life'),
        ('Na', 'Nature'),
        ('Kn', 'Knowledge'),
        ('Mo', 'Motivation'),
        ('In', 'Inspiration')
    ) 
    category = models.CharField(choices=CATEGORY_CHOICES)
    verified = models.BooleanField(default=False)
 

