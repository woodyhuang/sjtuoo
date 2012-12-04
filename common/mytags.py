#coding: utf-8

from django import template
from django.forms.fields import CheckboxInput
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, CheckboxInput)


def asmoney(amount):
    try:
        if isinstance(amount, str) or isinstance(amount, unicode):
            amount = float(amount)
        return '%s%s' % (floatformat(amount, 2), u'元')
    except:
        return amount
    
register.filter('asmoney', asmoney)