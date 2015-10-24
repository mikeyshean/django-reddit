from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import User, Sub, Post

class IndexView(generic.ListView):
    template_name = 'my_reddit/index.html'
    context_object_name = 'subs_list'

    def get_queryset(self):
        return Sub.objects.order_by('name')

class SubView(generic.DetailView):
    template_name = 'my_reddit/sub_show.html'
    model = Sub

    def get_queryset(self):
        return Sub.objects.prefetch_related("posts__author")

def post_view(request, sub_id, post_id):
    post = Post.objects.prefetch_related("comments__author").get(pk=post_id)
    return render(request, 'my_reddit/post_show.html', { 'post': post })
