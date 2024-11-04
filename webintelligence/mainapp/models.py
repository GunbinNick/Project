from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    parent_first_name = models.CharField(max_length=255)
    parent_last_name = models.CharField(max_length=255)
    statistics = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"