from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=100, unique = True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    age = models.PositiveIntegerField(default=25)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50,blank=True, null=True, default='Male')
    image = models.ImageField(upload_to='uploads/images/', default= 'default_human.jpg')
    address = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name