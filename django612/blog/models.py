from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):  # 类别
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):  # 标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)  # 标题
    body = models.TextField()   # 文章 TextField用于储存大段文章
    created_time = models.DateTimeField()  # 创建时间
    modified_time = models.DateTimeField()  # 最后一次修改时间

    excerpt = models.CharField(max_length=200, blank=True) # 文章摘要，参数可以为空

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 类别
    tags = models.ManyToManyField(Tag, blank=True)  # 标签

    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})
