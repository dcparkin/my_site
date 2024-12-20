from django import forms
from .models import BlogPost

# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea)
#     author_fn = forms.CharField()
#     author_ln = forms.CharField()
#     image = forms.ImageField()


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['slug', 'date']