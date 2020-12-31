from django import  template
from General_education_system.models import Category_education


register=template.Library()

@register.simple_tag()
def get_categories():
    return Category_education.objects.all()