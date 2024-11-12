from django.shortcuts import render
from enum import Enum
from django.http import Http404

class BlogPost():
    def __init__(self, title=None, blog_text=None, image=None) -> None:
        self.image = image
        self.title = title
        self.blog_text = blog_text
    
blogs = [
    BlogPost("Blog1", "This is Blog 1 and here is all the text"),
    BlogPost("Blog2", "This is Blog 2 and here is all the text"),
    BlogPost("Blog3", "This is Blog 3 and here is all the text"),
    BlogPost("Blog4", "This is Blog 4 and here is all the text")
]

# Create your views here.

# welcome page with 3 blog posts
def blog_index(request):
    
    content = {
        'first_three': blogs[:3],
    }
    return render(request, "blog/index.html", content) 

# list of all blog posts (/blog/posts)
def all_blog_posts(request):
    return render(request, "blog/all_blogs.html", {'all_blogs': blogs})

# view specific blog post (/blog/posts/blog_name)
def specific_blog_post(request, blog_name):
    try:
        blog = [b for b in blogs if b.title == blog_name][0]
        return render(request, "blog/show_blog.html", {'name' : blog_name, 
                                                   'blog': blog})
    except:
        raise Http404()
