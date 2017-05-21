from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag()
def get_theme():
    return settings.BOOTSTRAP_THEME


# ======================================================


@register.filter('fieldtype')
def fieldtype(field):
    return field.field.widget.__class__.__name__