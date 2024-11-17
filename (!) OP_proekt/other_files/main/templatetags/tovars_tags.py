# tovars = Products.objects.all()
# categories = Categorii.objects.all()

# 'categories': categories,
# "tovars": tovars,

from django import template

from tovars.models import Categorii, Products

register = template.Library()

@register.simple_tag()
def products():
      return Products.objects.all()

@register.simple_tag()
def category_tags():
      return Categorii.objects.all()