from django.contrib import admin
from django.urls import include, path
from blog.feeds import AllPostsRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('blog.urls')),
    path(r'', include('comments.urls')),
    path(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
]
