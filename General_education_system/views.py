from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from footer_project.models import \
    About_Company_Category,\
    AboutCompany,\
    Opportunities_category,\
    Oportunities,\
    Ourpartners,Ourpartners_category

from .models import Category_education,General_education_system,Floor,Dorm_building
from .forms import General_education_systemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from student.models import Dorm_room,Room,Dorm_building

# Create your views here.

def index(request):
    about_company_categories = About_Company_Category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    ourpartners_category = Ourpartners_category.objects.all()
    categories=Category_education.objects.annotate(cnt=Count('general_education_system'))

    context={
        'about_company_categories': about_company_categories,
        'oportunities_category': opportunities_categories,
        'ourpartners_category': ourpartners_category,
        'categories':categories,

    }
    return render(request,'education/base.html',context)



def get_education_category(request,pk):
    # используем функцию из templatetags
    # для отмены повторения  использовании катео
    categories=Category_education.objects.annotate(cnt=Count('general_education_system'))
    about_company_categories = About_Company_Category.objects.all()
    opportunities_categories = Opportunities_category.objects.all()
    ourpartners_category = Ourpartners_category.objects.all()
    education=General_education_system.objects.filter(category=pk)
    page=request.GET.get('page',1)
    paginator=Paginator(education,1)
    try:
        education=paginator.page(page)
    except PageNotAnInteger:
        education=paginator.page(1)
    except EmptyPage:
        education=paginator.page(paginator.num_pages)

    return render(request, 'category_education.html',
                  {
                      'about_company_categories': about_company_categories,
                      'oportunities_category': opportunities_categories,
                      'ourpartners_category': ourpartners_category,
                      'categories':categories,
                      'education': education,


                   })


def get_education_detail(request,pk):
    education=get_object_or_404(General_education_system,pk=pk)
    dorm_room=Dorm_room.objects.filter(pk=pk)
    # dorm_room_drom_building=Dorm_room.dorm_building.through.objects.filter(dorm_room_id=pk)
    General_education_system_door_room_name=General_education_system.objects.filter(door_room_name=pk)
    dorm_building=Dorm_building.objects.filter(dorm_room=pk)

    floor=Floor.objects.filter(dorm_bulding=pk)
    return render(request, 'category_education_read_more.html',
                  {''
                   'education':education,
                   'floor': floor,
                   'dorm_room':dorm_room,
                   'dorm_building':dorm_building,
                   # 'dorm_room_drom_building':dorm_room_drom_building,
                   'General_education_system_door_room_name':General_education_system_door_room_name})

def add_education_system(request):
    if request.method == 'POST':
        education=General_education_systemForm(request.POST,
                                               request.FILES)
        if education.is_valid():
            education_system=education.save()
            return redirect(education_system)
    else:
        education=General_education_systemForm()
    return render(request, 'add_education_system.html', {'form':education})


def get_dorm_building_detail(request,pk):
    # education=get_object_or_404(General_education_system,pk=pk)
    dorm_building=Dorm_building.objects.filter(dorm_room=pk)
    floor=Floor.objects.filter(dorm_bulding=pk)

    room=Room.objects.filter(floor=pk)
    # General_education_system_door_room_name=General_education_system.objects.get(door_room_name=pk)
    context={
        'dorm_building':dorm_building,
        'floor':floor,















        'room':room
        # 'education': education,
        # 'General_education_system_door_room_name': General_education_system_door_room_name

    }
    return render(request,'dorm_room_detail/index.html',context)

