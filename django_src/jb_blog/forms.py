from django import forms
from django.contrib.auth.models import User
from .models import Post
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):

    	class Meta:

       		model = Post
       		fields = ('title', 'abstract',)

