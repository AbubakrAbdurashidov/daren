from django import template

from article.models import Article

register = template.Library()


@register.simple_tag
def last_three_articles():
    return Article.objects.order_by('-id')[:3]