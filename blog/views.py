from typing import Any
from django.shortcuts import render, get_object_or_404
from django.core.files import File
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from enum import Enum
from django.http import HttpResponseRedirect

from .models import BlogPost, Author
from .forms import BlogPostForm
    


# Create your views here.

# welcome page with 3 blog posts
class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['first_three'] = BlogPost.objects.all().order_by("-date")[:3]
        return context

# list of all blog posts (/blog/posts)
class AllPostsView(ListView):
    template_name = "blog/all_blogs.html"
    model = BlogPost
    ordering = ['-date']
    context_object_name = 'all_blogs'

# view specific blog post (/blog/posts/blog_name)
class ViewPostView(DetailView):
    template_name = "blog/show_blog.html"
    model = BlogPost


class CreatePostView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/create_blog.html"
    success_url = "/"

