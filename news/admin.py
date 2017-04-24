from django.contrib import admin
from .models import Article, PriceList

admin.site.register(Article)
admin.site.register(PriceList)
admin.site.register(Comment)
