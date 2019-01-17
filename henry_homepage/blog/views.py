from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from django.db.models import Q
from taggit.models import  Tag
from django import forms
from django.forms.models import modelform_factory
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean
from haystack.generic_views import SearchView
from . models import Post

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.template_name = 'blog/index.html'
        # Filter by tag
        if( 'tag' in self.kwargs.keys() ):
            post_list = Post.objects.filter(tags__name=self.kwargs['tag']).order_by('-published_date')
            '''
            self.template_name = 'search/search_page.html'
            query = self.request.GET.get('q')
            post_list = SearchQuerySet().autocomplete(tags=query).order_by('-published_date')
            '''
        elif( self.request.GET.get('q') ):
            self.template_name = 'search/search_page.html'
            query = self.request.GET.get('q')
            #post_list = SearchQuerySet().autocomplete(content_auto=query)
            post_list = SearchQuerySet().autocomplete(content__contains=query).order_by('-published_date')
        else:
            post_list = Post.objects.all().order_by('-published_date')
        return post_list

    def get_context_data(self, **kwargs):
        # Variable
        page_header_message = ''
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tags'] = Tag.objects.all()
        #
        if( 'tag' in self.kwargs.keys() ):
            page_header_message = "Posts tagged by " + self.kwargs['tag']
            context['tag'] = self.kwargs['tag']
        elif( self.request.GET.get('q') ):
            page_header_message = "Posts contains " + self.request.GET.get('q')
            context['query'] = self.request.GET.get('q')
        else:
            page_header_message = "Welcome to Henry's Blog"
        context['page_header_message'] = page_header_message
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
    template_name_suffix = '_template'

    form_class = modelform_factory(Post,
            exclude=['created_date', 'published_date'],
            widgets = {'title': forms.TextInput(attrs={'size':100}),
                       'author': forms.TextInput(attrs={'size':100}),
                      }
            )

class PostUpdateView(UpdateView):
    model = Post
    template_name_suffix = '_template'

    form_class = modelform_factory(Post,
            exclude=['created_date', 'published_date'],
            widgets = {'title': forms.TextInput(attrs={'size':100}),
                       'author': forms.TextInput(attrs={'size':100}),
                      }
            )

class PostDeleteView(DeleteView):
    model = Post
    # FIXME: no use of the template_name
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy( 'blog:index' )

