from django.conf.urls import url
from . import views


app_name = 'news'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'contacts/', views.ContactsView.as_view(), name='contacts'),
    url(r'about/$', views.about, name='about'),
    url(r'about/(?P<comment_page>[0-9]*)/', views.about, name='about'),
    #url(r'about/', views.AboutView.as_view(), name='about'),
    url(r'add_comment/', views.get_comment, name='comment'),
    url(r'pricelist/(?P<pk>[0-9]+)?', views.PriceListView.as_view(),
        name='pricelist'),
 
]
