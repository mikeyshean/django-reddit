from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import User, Sub, Post, Comment
from django.db.models import Prefetch

class IndexView(generic.ListView):

    def get(self, request):
        template_name = 'my_reddit/base.html'
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

    def get(self, request, *args, **kwargs):
        template_name = 'my_reddit/sub_show.html'
        sub = get_object_or_404(
            Sub.objects.prefetch_related(
                Prefetch('posts', to_attr='sub_posts'),
                'sub_posts__votes',
                'sub_posts__author'
            ), pk=kwargs['pk']
        )

        post_details = sub.posts_with_votes()

        return render(request, template_name, { 'sub': sub, 'posts': post_details })

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        text = request.POST['text']
        sub_id = request.POST['sub_id']

        post = Post.objects.create(title=title, text=text, sub_id=sub_id, author_id=1)
        return HttpResponseRedirect(reverse('my_reddit:post', args=(sub_id,post.id)))

def new_post(request, sub_id):
    return render(request, 'my_reddit/new_post.html', { 'sub_id': sub_id })

def post_view(request, sub_id, post_id):
    post = get_object_or_404(Post.objects.select_related("sub"), pk=post_id)
    comments_dict = post.comments_by_parent_id()

    return render(
        request,
        'my_reddit/post_show.html',
        { 'post': post, 'comments': comments_dict, 'nav_sub': post.sub }
    )

def comment_vote(request, comment_id, type):
    comment = get_object_or_404(Comment, pk=comment_id)

    if type == 'upvote':
        comment.votes.create(amount=1)
    elif type =='downvote':
        comment.votes.create(amount=-1)
    post = comment.post

    return HttpResponseRedirect(
        reverse('my_reddit:post', args=(post.sub_id, post.id))
    )

def post_vote(request, sub_id, post_id, type):
    post = get_object_or_404(Post, pk=post_id)
    if type == 'upvote':
        post.votes.create(amount=1)
    elif type =='downvote':
        post.votes.create(amount=-1)

    return HttpResponseRedirect(
        reverse('my_reddit:sub', args=(post.sub_id,))
    )


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
        new_comment = parent.child_comments.create(
            comment_text=request.POST['comment_text'],
            author_id=1,
            post_id=parent.post_id
        )

        return HttpResponseRedirect(
            reverse('my_reddit:comment', args=(new_comment.id,))
        )


def parent_comment(request, sub_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comments.create(
        comment_text=request.POST['comment_text'],
        author_id=1
    )

    return HttpResponseRedirect(
        reverse('my_reddit:post', args=(sub_id,post_id))
    )
