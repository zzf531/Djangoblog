from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ii/$', views.ii, name='ii'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^search/$', views.search, name='search'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
