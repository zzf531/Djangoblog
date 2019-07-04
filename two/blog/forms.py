from django import forms
from .models import Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author']

