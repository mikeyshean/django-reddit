from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=50)


class Sub(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User)

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    sub = models.ForeignKey(Sub)
