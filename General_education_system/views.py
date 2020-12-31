from django.shortcuts import render

from footer_project.models import AboutCompany,Oportunities
from .models import General_education_system,Category_education

# Create your views here.


def index(request):
    categories=Category_education.objects.all()
    company = AboutCompany.objects.all()
    oportunities=Oportunities.objects.all()

    context={
        'categories':categories,
        'company':company,
        'oportunities':oportunities
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
    education=General_education_system.objects.filter(category=pk)
    return render(request, 'test.html',
                  {
                      # 'categories':categories,
                      'education': education,
                   })
