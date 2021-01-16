from django.shortcuts import render, get_object_or_404

from footer_project.models import \
    About_Company_Category,\
    AboutCompany,\
    Opportunities_category,\
    Oportunities,\
    Ourpartners,Ourpartners_category
from General_education_system.models import Category_education
from django.views import generic

# Create your views here.

# используем templatetags- для сокращения повторения кода
# def home(request):
#     # categories=Category_education.objects.all()
#     # about_company_categories=About_Company_Category.objects.all() (путь в templatetags)
#     # opportunities_categories=Opportunities_category.objects.all() (путь в templatetags)
#     # ourpartners_category=Ourpartners_category.objects.all()
#     context={
#         # 'about_company_categories':about_company_categories,
#         # 'oportunities_category':opportunities_categories,
#         # 'ourpartners_category':ourpartners_categoryб
#         # 'categories': categories,
#
#     }
#     return render(request,'education/base.html',context)



#аналог вверхнего
class Home(generic.ListView):
    template_name = 'education/base.html'

    def get_queryset(self):
        categories = Category_education.objects.all()
        about_company_categories = About_Company_Category.objects.all()
        opportunities_categories = Opportunities_category.objects.all()
        ourpartners_category = Ourpartners_category.objects.all()

        context={
            'about_company_categories': about_company_categories,
            'oportunities_category': opportunities_categories,
            'ourpartners_category': ourpartners_category,
            'categories': categories,

        }
        return context

################################################################
################################################################

# def get_about_company_category_footer(request, pk):
#     about_company=AboutCompany.objects.filter(category=pk)
#     # about_company_categories = About_Company_Category.objects.all() (путь в templatetags)
#     # opportunities_categories = Opportunities_category.objects.all() (путь в templatetags)
#     # ourpartners_category = Ourpartners_category.objects.all() (путь в templatetags)
#     categories=Category_education.objects.all()
#     context={
#         'about_company':about_company,
#         # 'about_company_categories': about_company_categories,
#         # 'oportunities_category': opportunities_categories,
#         # 'ourpartners_category': ourpartners_category,
#         'categories':categories
#
#
#     }
#     return  render(request, 'footer_project/about_company.html', context)

# аналог верхнего
class AboutCompanyCategoryFooter(generic.ListView):
    model = AboutCompany
    template_name = 'footer_project/about_company.html'


    def get_queryset(self):
        return AboutCompany.objects.filter(category=self.kwargs['pk'])

#######################################################################
#######################################################################

# def get_opportunities_footer(request,pk):
#     categories=Category_education.objects.all()
#     oportunities=Oportunities.objects.filter(category=pk)
#     about_company_categories = About_Company_Category.objects.all()
#     opportunities_categories = Opportunities_category.objects.all()
#     ourpartners_category = Ourpartners_category.objects.all()
#     context={
#         'categories': categories,
#         'ourpartners_category': ourpartners_category,
#         'oportunities_category': opportunities_categories,
#         'about_company_categories': about_company_categories,
#         'oportunities':oportunities
#     }
#     return render(request,'footer_project/oportunities.html', context)

# аналог верхнего
class Oportunities_footer(generic.ListView):
    model = Oportunities
    template_name = 'footer_project/oportunities.html'

    def get_queryset(self):
        return Oportunities.objects.filter(category=self.kwargs['pk'])

#####################################################################
#####################################################################

# def get_ourpartners(request,pk):
#     ourpartners_category = Ourpartners_category.objects.all()
#     opportunities_categories = Opportunities_category.objects.all()
#     about_company_categories = About_Company_Category.objects.all()
#     categories=Category_education.objects.all()
#     ourpartners=Ourpartners.objects.filter(category=pk)
#     context={
#         'ourpartners_category': ourpartners_category,
#         'oportunities_category': opportunities_categories,
#         'ourpartners':ourpartners,
#         'about_company_categories': about_company_categories,
#         'categories': categories,
#
#     }
#     return render(request, 'footer_project/ourpartners.html',context)
# аналог вверхнего
class Ourpartners_footer(generic.ListView):
    model = Ourpartners
    template_name = 'footer_project/ourpartners.html'

    def get_queryset(self):
        return Ourpartners.objects.filter(category=self.kwargs['pk'])