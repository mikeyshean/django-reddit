from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import User, Sub, Post, Comment

class IndexView(generic.ListView):

    def get(self, request):
        template_name = 'my_reddit/index.html'
        subs_list = Sub.objects.order_by('name')
        return render(request, template_name, { 'subs_list': subs_list })

    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        sub = Sub.objects.create(name=name, description=description, creator_id=1)
        return HttpResponseRedirect(reverse('my_reddit:sub', args=(sub.id,)))

def new_sub(request):
    return render(request, 'my_reddit/new_sub.html')

class SubView(generic.DetailView):
    template_name = 'my_reddit/sub_show.html'

    def get_queryset(self):
        return Sub.objects.prefetch_related("posts__author")

class CommentView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        post = comment.post
        return render(
            request,
            'my_reddit/comment.html',
            { 'comment': comment, 'post': post }
        )

    def post(self, request, *args, **kwargs):
        parent = get_object_or_404(Comment, pk=kwargs['pk'])
        parent.child_comments.create(
            comment_text=request.POST['comment_text'],
            author_id=1,
            post_id=parent.post_id
        )

        return HttpResponseRedirect(reverse('my_reddit:comment', args=(parent.id,)))


def post_view(request, sub_id, post_id):
    ## Work on pre-fetching nested comments:

    # top_level_comments = Comment.objects.filter(parent_id=null)
    # post = Post.objects.prefetch_related(
    #     Prefetch(
    #         "comments__author",
    #         queryset=top_level_comments,
    #         to_attr='top_comments'
    #     )).get(pk=post_id)

    post = Post.objects.prefetch_related("comments__author").get(pk=post_id)
    return render(request, 'my_reddit/post_show.html', { 'post': post })

def parent_comment(request, sub_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comments.create(
        comment_text=request.POST['comment_text'],
        author_id=1
    )

    return HttpResponseRedirect(reverse('my_reddit:post', args=(sub_id,post_id)))
