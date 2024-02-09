from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Article


class BlogListView(ListView):
    model = Article
    extra_context = {
        'title': 'Блог'
    }


class BlogDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object