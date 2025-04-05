from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    image= models.ImageField(upload_to='teacher/',  null=True, blank=True)
    description = models.TextField(max_length=300)  



    def __str__(self):
        return self.name


class Users(AbstractUser):
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)   
    address = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.first_name  
    


class Saqlovchi(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)    
    message = models.TextField()
    def __str__(self):
        return self.first_name
    



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Kurs(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='kurs/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name        


class Banner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    




class Blog(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    day = models.DateField()
    image = models.ImageField(upload_to='blog/')
    






class Gallery(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')    


