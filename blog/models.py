from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"  


# Create your models here.
class BlogPost(models.Model):
    image = models.ImageField(upload_to="blog_pics")
    title = models.CharField(max_length=50)
    blog_text = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="blogs")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="",  blank=True, 
                            null=False, db_index=True)

    def get_blog_url(self):
        return reverse("blog-post", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    