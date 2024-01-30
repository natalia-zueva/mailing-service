from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Article


class BlogListView(ListView):
    model = Article
    extra_context = {
        'title': 'Блог'
    }
