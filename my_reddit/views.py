from django.shortcuts import render
from django.views import generic
from .models import User, Sub, Post

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'my_reddit/index.html'
    context_object_name = 'subs_list'

    def get_queryset(self):
        return Sub.objects.order_by('name')
