from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def get_values(dict, key):
    return dict.get(key)
