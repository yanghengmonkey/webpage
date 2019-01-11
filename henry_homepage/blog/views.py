from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import render
from . models import Post

class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(DetailView, pk):
    model = Post
    template_name = 'blog/detail.html'

class PostCreate(CreateView):
    model = Post
    fields = [
         'author'
        ,'title'
        ,'text'
        ,'created_date'
        ,'published_date'
    ]

class PostUpdate(UpdateView):
    model = Post
    fields = [
        'author'
        ,'title'
        ,'text'
        ,'created_date'
        ,'published_date'
    ]

class PostDelete(DetailView):
    post = Post
    sucess_url = reverse_lazy( 'blog:index' )
