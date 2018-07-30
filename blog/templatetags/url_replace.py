# https://gist.github.com/sumitlni/4f308e5999d2d4d8cb284fea7bf0309c#file-url_replace-py
from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    query_string = request.GET.copy()
    query_string[field] = value * 8
    
    return query_string.urlencode()