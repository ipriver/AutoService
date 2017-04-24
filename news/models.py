from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    article_descr = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)


class PriceList(models.Model):
    transp_type = models.CharField(max_length=50)
    price = models.IntegerField(default=0)


class Comment(models.Model):
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)