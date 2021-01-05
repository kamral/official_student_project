from django import template
from footer_project.models import \
    About_Company_Category,\
    Opportunities_category,\
    Ourpartners_category




register=template.Library()

@register.simple_tag()
def get_about_company_categories(name='get_about_company_categories'):
    return About_Company_Category.objects.all()

@register.simple_tag()
def get_oportunities_categories():
    return Opportunities_category.objects.all()

@register.simple_tag()
def get_ourpartners_category():
    return  Ourpartners_category.objects.all()


@register.inclusion_tag('templatetags_categories_footer/about_company_categories.html')
def show_categories_about_company():
    categories=About_Company_Category.objects.all()
    return {'about_company_categories':categories}


@register.inclusion_tag('templatetags_categories_footer/oportunities_category.html')
def show_categories_oportunities_category():
    categories=Opportunities_category.objects.all()
    return {'oportunities_category':categories}


@register.inclusion_tag('templatetags_categories_footer/ourpartners_category.html')
def show_ourpartners_category():
    category=Ourpartners_category.objects.all()
    return {'ourpartners_category':category}























