from django.db import models
from collections import defaultdict

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
    text = models.CharField(max_length=2000)
    author = models.ForeignKey(User)
    sub = models.ForeignKey(Sub, related_name='posts', related_query_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def comments_by_parent_id(self):
        result = {}
        result = defaultdict(lambda:[], result)

        for comment in self.comments.all().prefetch_related("author"):
            result[comment.parent_id].append(comment)

        return dict(result)


class Comment(models.Model):
    comment_text = models.CharField(max_length=2500)
    author = models.ForeignKey(User)
    parent = models.ForeignKey('self', default=None, null=True, related_name='child_comments')
    post = models.ForeignKey(Post, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text
