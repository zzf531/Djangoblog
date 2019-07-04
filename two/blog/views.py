import markdown
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from comment.forms import CommentForm
from .models import Post, Category, Tag
from .forms import BlogForm


# 首页
def index(request):
    return render(request, 'blog/index.html', context={
                      'title': '我的博客首页',
                  })


# 所有文章
def post(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'post_list': post_list,
        'yeme': '所有文章',
    })


# 详细内容
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    contexts = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blog/detail.html', context=contexts)


# 前端
def post1(request):
    post_list = Post.objects.filter(category__name='前端').order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'post_list': post_list,
        'yeme': '所有文章',
    })


# 后端
def post2(request):
    post_list = Post.objects.filter(category__name='后端').order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'post_list': post_list,
        'yeme': '所有文章',
    })


# 社区
def post3(request):
    post_list = Post.objects.filter(category__name='社区').order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'post_list': post_list,
        'yeme': '所有文章',
    })


# 分享
def post4(request):
    post_list = Post.objects.filter(category__name='分享').order_by('-created_time')
    return render(request, 'blog/post.html', context={
        'post_list': post_list,
        'yeme': '所有文章',
    })


