from django.db import models
from django.contrib.auth.hashers import make_password

class Teacher(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    parent_first_name = models.CharField(max_length=100)
    parent_last_name = models.CharField(max_length=100)
    statistics = models.TextField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"