from django.shortcuts import render

from footer_project.models import \
    AboutUs,Contacts,Answers,Questions
from .models import General_education_system,Category_education

# Create your views here.


def index(request):
    categories=Category_education.objects.all()
    about_us=AboutUs.objects.get(pk__in=[1])
    contacts=Contacts.objects.get(pk__in=[1])
    answers=Answers.objects.get(pk__in=[1])
    questions= Questions.objects.get(pk__in=[1])

    context={
        'answers': answers,
        'questions': questions,
        'categories':categories,
        'about_us':about_us,
        'contacts': contacts,
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
    about_us=AboutUs.objects.all()
    contacts=Contacts.objects.all()
    about_company=AboutCompany.objects.all()
    return render(request, 'test.html',
                  {
                      # 'categories':categories,
                      'education': education,
                      'about_us':about_us,
                      'contacts':contacts,
                      'about_company':about_company
                   })

