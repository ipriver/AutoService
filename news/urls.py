from django.conf.urls import url
from . import views


app_name = 'news'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'contacts/', views.ContactsView.as_view(), name='contacts'),
    url(r'about/', views.AboutView.as_view(), name='about'),
    url(r'pricelist/', views.PriceListView.as_view(), name='pricelist'),
    url(r'(?P<id_key>[0-9])/(?P<p2_key>[0-9])', views.tr),
]
