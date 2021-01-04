from django.shortcuts import render
from footer_project.models import \
    About_Company_Category,\
    AboutCompany,\
    Opportunities_category,\
    Oportunities,\
    Ourpartners,Ourpartners_category

from .models import Category_education,General_education_system

# Create your views here.


def index(request):
    about_company_categories = About_Company_Category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    ourpartners_category = Ourpartners_category.objects.all()
    categories=Category_education.objects.all()

    context={
        'about_company_categories': about_company_categories,
        'oportunities_category': opportunities_categories,
        'ourpartners_category': ourpartners_category,
        'categories':categories,

    }
    return render(request,'education/base.html',context)

# def get_category(request,category_id):
#     pass


# def get_category(request,category_id):
#     general_education_system=General_education_system.objects.filter(category_id)
#     categories=Category_education.objects.all()
#     category=Category_education.objects.get(pk=category_id)
#     return render(request,'eduction_category.html',{
#         'general_education_system':general_education_system,
#         'categories':categories,
#         'category':category
#
#     })


def get_education_category(request,pk):
    # используем функцию из templatetags
    # для отмены повторения  использовании катео
    # categories=Category_education.objects.all()
    about_company_categories = About_Company_Category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    ourpartners_category = Ourpartners_category.objects.all()
    education=General_education_system.objects.filter(category=pk)


    return render(request, 'category_education.html',
                  {
                      'about_company_categories': about_company_categories,
                      'oportunities_category': opportunities_categories,
                      'ourpartners_category': ourpartners_category,
                      # 'categories':categories,
                      'education': education,


                   })



