from django.contrib import admin
from .models import BlogPost, Author

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "author")
    list_display = ("title", "author")

# class AuthorAdmin(admin.ModelAdmin):


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author)
