from django import template
from ..models import Post, Category

register = template.Library()


@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档 模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()
