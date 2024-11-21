from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from articles.models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content',)
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'author')
    template_name = 'article_new.html'
