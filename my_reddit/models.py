from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    sub = models.ForeignKey(Sub, related_name='posts', related_query_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
