from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from django.db.models import Q
from taggit.models import  Tag
from . models import Post

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-published_date']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tags'] = Tag.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tags'] = Tag.objects.all()
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = [
        'author'
        ,'title'
        ,'content'
        ,'created_date'
        ,'published_date'
    ]

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/create.html'
    fields = [
        'author'
        ,'title'
        ,'content'
        ,'created_date'
        ,'published_date'
    ]

class PostDeleteView(DeleteView):
    model = Post
    # FIXME: no use of the template_name
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy( 'blog:index' )

# TEMP
def tagpage(request, tag):
    post_list = Post.objects.filter(tags__name=tag)
    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    context = {
        'posts': paginator.get_page(page),
        'tags' : Tag.objects.all(),
        'tag' : tag
    }
    return render_to_response("blog/tagpage.html",  context )


def search(request):
    template_name = 'blog/search_page.html'
    query = request.GET.get('q')
    post_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')

    context = {
        'posts': paginator.get_page(page),
        'query': query,
        'tags' : Tag.objects.all()
    }
    return render(request, template_name, context)

