from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    Price = models.CharField(max_length=255)
    Description = models.CharField(max_length=400)
    Color = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.Name
    
