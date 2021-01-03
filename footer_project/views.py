from django.shortcuts import render

from footer_project.models import \
    About_Company_Category,\
    AboutCompany,\
    Opportunities_category,\
    Oportunities,\
    Ourpartners,Ourpartners_category

# Create your views here.


def index(request):
    about_company_categories=About_Company_Category.objects.all()
    opportunities_categories=Opportunities_category.objects.all()
    ourpartners_category=Ourpartners_category.objects.all()
    context={

        'about_company_categories':about_company_categories,
        'oportunities_category':opportunities_categories,
        'ourpartners_category':ourpartners_category
    }
    return render(request,'education/base.html',context)
