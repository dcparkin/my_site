from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name="blog-home"),
    path('posts', views.all_blog_posts, name="all-posts"),
    path('posts/<str:blog_name>', views.specific_blog_post, name="blog-post"),
]


