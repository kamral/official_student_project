from django import template
from student.models import Floor
from django.db.models import Count

register=template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Floor.objects.all()