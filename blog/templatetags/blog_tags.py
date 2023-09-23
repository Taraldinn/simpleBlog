from django import template
from ..models import Post

from django.db.models import Count 

register = template.Library()

@register.simple_tag(name='Posts_count')
def total_posts():
    published = Post.objects.filter(Status='pub').count()
    return published
