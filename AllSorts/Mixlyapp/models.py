from django.db import models

# Create your models here.

class customerdata(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Message=models.TextField()