from django import template
from ..models import Post, Category

register = template.Library


@register.simple_tag
def archives():
    return Category.objects.all()
