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


# ======================================================


@register.filter("add_label_class")
def add_label_class(field, css_class):
    if not field:
        return 'Field label does not exist'
    else:
        return field.label_tag(attrs={'class': css_class})


# ======================================================


@register.filter("add_input_class")
def add_input_class(field, css_class):
    if not field:
        return 'Field does not exist'
    else:
        return field.as_widget(attrs={"class": css_class})

