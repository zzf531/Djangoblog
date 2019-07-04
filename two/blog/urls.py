from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 网站主页
    url(r'^index/$', views.index, name='index'),  # 网站主页
    url(r'post/$', views.post, name='post'),  # 文章集合的页面
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),  # 文章的详细页面
    url(r'post1/$', views.post1, name='post1'),  # 分类标签 前端
    url(r'post2/$', views.post2, name='post2'),  # 分类标签 后端
    url(r'post3/$', views.post1, name='post3'),  # 分类标签 社区
    url(r'post4/$', views.post2, name='post4'),  # 分类标签 分享
]