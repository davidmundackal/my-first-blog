"""mysite form Configuration

   necessary imports

   PostForm: Name of our form

"""
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # model should be used to create this form(model = Post).
    class Meta:
        model = Post
        fields = ('title', 'text',)
