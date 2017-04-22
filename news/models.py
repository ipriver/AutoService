from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    article_descr = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    x = models.IntegerField(default=0)

    def mod_x(self):
        self.x += 10
        print('hello', self.x)
