from django import forms
from .models import About_Comment
from django.utils.translation import ugettext_lazy as _


class CommentForm(forms.Form):
    title = forms.CharField(error_messages={'required': ''}, label='Тема комментария:', max_length=50)
    author = forms.CharField(error_messages={'required': ''}, label='Ваше имя:', max_length=50)
    comment = forms.CharField(error_messages={'required': ''}, label='Комментарий:', max_length=250, widget=forms.Textarea(attrs={'rows':6,
                                            'cols':30,
                                            'style':'resize:none;'}))
