from django import template
from posts.models import Category

register = template.Library()


@register.simple_tag(name='categories')
def get_categories():
    return Category.objects.all()