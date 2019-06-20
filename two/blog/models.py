from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 文章
class Post(models.Model):
    title = models.CharField(max_length=100) # 标题
    body = models.TextField()  # 文章主体
    created_time = models.DateTimeField()  # 创建时间
    modified_time = models.DateTimeField()  # 修改时间

    excerpt = models.CharField(max_length=200)  # 文章的摘要

    category = models.ForeignKey(Category, on_delete=models.CASCADE)   # 分类
    tags = models.ManyToManyField(Tag, blank=True)  # 标签

    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

