import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag


def index(request):
    return render(request, 'blog/index.html', context={
                      'title': '我的博客首页',
                  })


def post(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'title': '你的博客',
        'post_list': post_list,
        'yeme': '所有文章',
        'mingyan': '但行好事，莫问前程',
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={
        'post': post,
        'yeme': '文章详情',
    })


def post1(request):
    post_list = Post.objects.filter(category__name='前端').order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'title': '你的博客',
        'post_list': post_list,
        'yeme': '所有文章',
        'mingyan': '但行好事，莫问前程',
    })


def post2(request):
    post_list = Post.objects.filter(category__name='后端').order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'title': '你的博客',
        'post_list': post_list,
        'yeme': '所有文章',
        'mingyan': '但行好事，莫问前程',
    })



