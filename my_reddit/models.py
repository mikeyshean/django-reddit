from django.db import models
from collections import defaultdict
from django.db.models import Sum
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class TimestampsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimestampsModel):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sub(TimestampsModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Vote(TimestampsModel):
    amount = models.SmallIntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

class Post(TimestampsModel):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)
    author = models.ForeignKey(User)
    sub = models.ForeignKey(Sub, related_name='posts', related_query_name='post')
    votes = GenericRelation(Vote)

    def __str__(self):
        return self.title

    def comments_by_parent_id(self):
        result = {}
        result = defaultdict(lambda:[], result)

        for comment in self.comments.all().prefetch_related("author", "votes"):
            comment_details = {'comment': comment}
            vote_count = comment.vote_count()['vote_count']

            if vote_count is not None:
                comment_details['vote_count'] = vote_count
            else:
                comment_details['vote_count'] = 0

            result[comment.parent_id].append(comment_details)
    
        return dict(result)

    def vote_count(self):
        return self.votes.aggregate(vote_count=Sum('amount'))


class Comment(TimestampsModel):
    comment_text = models.CharField(max_length=2500)
    author = models.ForeignKey(User)
    parent = models.ForeignKey('self', default=None, null=True, related_name='child_comments')
    post = models.ForeignKey(Post, related_name='comments')
    votes = GenericRelation(Vote)

    def __str__(self):
        return self.comment_text

    def vote_count(self):
        return self.votes.aggregate(vote_count=Sum('amount'))
