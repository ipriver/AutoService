from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    article_descr = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)
    
