from django import template
from student.models import Floor
from django.db.models import Count

register=template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Floor.objects.all()

@register.inclusion_tag('dorm_room_detail/list_categories_floor.html')
def show_categories():
    categories = Floor.objects.annotate(cnt=Count('room')).filter(cnt__gt=0)
    return {'categories': categories}
