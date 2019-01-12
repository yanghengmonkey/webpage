from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from django.db.models import Q
from . models import Post

class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(DetailView):
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

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("blog/tagpage.html", {'posts': posts, 'tag': tag} )


def search(request):
    template_name = 'blog/search_page.html'
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {
        'posts': posts,
        'query': query
    }
    return render(request, template_name, context)
