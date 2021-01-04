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
    return  render(request, 'footer_project/about_us.html', context)



def get_about_company_category_footer_contacts(request, pk):
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
    return  render(request, 'footer_project/contacts.html', context)
