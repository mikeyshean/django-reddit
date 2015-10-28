from tastypie.resources import ModelResource
from my_reddit.models import Sub, Post, Comment


class SubResource(ModelResource):
    class Meta:
        queryset = Sub.objects.all()
        resource_name = 'sub'
        allowed_methods = ['get', 'post']

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        allowed_methods = ['get', 'post']

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        allowed_methods = ['get', 'post']
