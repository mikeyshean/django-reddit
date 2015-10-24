from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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

def top_level_comment(request, sub_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comments.create(
        comment_text=request.POST['comment_text'],
        author_id=1
    )

    return HttpResponseRedirect(reverse('my_reddit:post', args=(sub_id,post_id)))
