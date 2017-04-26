from django import forms
from .models import About_Comment


class CommentForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    author = forms.CharField(label='author', max_length=50)
    comment = forms.CharField(label='comment', max_length=250)

    
