from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"