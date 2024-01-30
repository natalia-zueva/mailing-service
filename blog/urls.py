from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list')
]