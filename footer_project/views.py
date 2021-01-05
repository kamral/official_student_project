from django.shortcuts import render

from footer_project.models import \
    About_Company_Category,\
    AboutCompany,\
    Opportunities_category,\
    Oportunities,\
    Ourpartners,Ourpartners_category
from General_education_system.models import Category_education

# Create your views here.


def home(request):
    categories=Category_education.objects.all()
    about_company_categories=About_Company_Category.objects.all()
    opportunities_categories=Opportunities_category.objects.all()
    ourpartners_category=Ourpartners_category.objects.all()
    context={
        'about_company_categories':about_company_categories,
        'oportunities_category':opportunities_categories,
        'ourpartners_category':ourpartners_category
    }
    return render(request,'education/base.html',context)


def get_about_company_category_footer(request, pk):
    categories=Category_education.objects.all()
    about_company=AboutCompany.objects.filter(category=pk)
    about_company_categories = About_Company_Category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    ourpartners_category = Ourpartners_category.objects.all()
    categories=Category_education.objects.all()
    context={
        'about_company':about_company,
        'about_company_categories': about_company_categories,
        'oportunities_category': opportunities_categories,
        'ourpartners_category': ourpartners_category,
        'categories':categories


    }
    return  render(request, 'footer_project/about_company.html', context)





def get_opportunities_footer(request,pk):
    categories=Category_education.objects.all()
    oportunities=Oportunities.objects.filter(category=pk)
    about_company_categories = About_Company_Category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    ourpartners_category = Ourpartners_category.objects.all()
    context={
        'categories': categories,
        'ourpartners_category': ourpartners_category,
        'oportunities_category': opportunities_categories,
        'about_company_categories': about_company_categories,
        'oportunities':oportunities
    }
    return render(request,'footer_project/oportunities.html', context)


def get_ourpartners(request,pk):
    ourpartners_category = Ourpartners_category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    about_company_categories = About_Company_Category.objects.all()
    categories=Category_education.objects.all()
    ourpartners=Ourpartners.objects.filter(category=pk)
    context={
        'ourpartners_category': ourpartners_category,
        'oportunities_category': opportunities_categories,
        'ourpartners':ourpartners,
        'about_company_categories': about_company_categories,
        'categories': categories,

    }
    return render(request, 'footer_project/ourpartners.html',context)