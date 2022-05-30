from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=20)


class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Event(models.Model):

    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    paid = models.BooleanField(null=True)
    image = models.FileField(null=True)
    published = models.BooleanField(null=True)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Book_ground(models.Model):

    bid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=20)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    paid = models.BooleanField(null=True)
    image = models.ImageField(null=True)
    published = models.BooleanField(null=True)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
