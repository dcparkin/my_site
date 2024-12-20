from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="blog-home"),
    path('posts', views.AllPostsView.as_view(), name="all-posts"),
    path('posts/<str:slug>', views.ViewPostView.as_view(), name="blog-post"),
    path('create-new', views.CreatePostView.as_view(), name="create-new-post"),

]


