from tastypie.resources import ModelResource
from my_reddit.models import Sub, Post, Comment
from django.db.models import Prefetch

class SubResource(ModelResource):
    class Meta:
        queryset = Sub.objects.all().prefetch_related(
            Prefetch('posts', to_attr='sub_posts'),
            'sub_posts__votes',
            'sub_posts__author'
        ).order_by('name')
        resource_name = 'sub'
        allowed_methods = ['get', 'post']

    def dehydrate(self, bundle):
        if self.get_resource_uri(bundle) == bundle.request.path:
            bundle.data['posts'] = []
            for post in bundle.obj.posts.all():
                resp = {}
                resp['title'] = post.title
                resp['author'] = post.author
                resp['vote_count'] = post.vote_count()['vote_count']
                bundle.data['posts'].append(resp)

        return bundle

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        allowed_methods = ['get', 'post']

    def dehydrate(self, bundle):
        bundle.data['vote_count'] = bundle.obj.vote_count()
        return bundle

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        allowed_methods = ['get', 'post']
