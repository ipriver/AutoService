from django.conf.urls import url
from . import views


app_name = 'news'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<id_key>[0-9])/(?P<p2_key>[0-9])', views.tr)
]
