from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import User, Sub, Post

class IndexView(generic.ListView):
    template_name = 'my_reddit/index.html'
    context_object_name = 'subs_list'

    def get_queryset(self):
        return Sub.objects.order_by('name')

# def sub_view(request, sub_id):
#     template_name = 'my_reddit/sub_show.html'
#     context_object_name = 'sub'
#
#     def get_queryset(self):
#         return Sub.objects.get(pk=sub_id).select_related('creator__name')
#

class SubView(generic.DetailView):
    template_name = 'my_reddit/sub_show.html'
    model = Sub

    def get_queryset(self):
        return Sub.objects.select_related('creator__name')
