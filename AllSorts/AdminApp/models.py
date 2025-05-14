from django.db import models

# Create your models here.

class Momentodata(models.Model):
    Certificatename=models.CharField(max_length=25)
    Position=models.CharField(max_length=30)
    image=models.ImageField(upload_to='image')
    Date=models.DateField()
    description=models.TextField(max_length=150)


class Profiledata(models.Model):
    image=models.ImageField(upload_to='image')
    Name=models.CharField(max_length=20)
    Email=models.EmailField()

    def __str__(self):
        return self.Name   
    
    def clean(self):
        super().clean()