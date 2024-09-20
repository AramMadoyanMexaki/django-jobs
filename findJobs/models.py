from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    salary = models.FloatField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.title
    

class JobUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=100, null=True)
