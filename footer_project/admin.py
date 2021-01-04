from django.contrib import admin
from .models import Ourpartners,\
    AboutCompany,\
    Oportunities,\
    About_Company_Category,\
    Opportunities_category,Ourpartners_category
# Register your models here.


class AboutCompanyCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(About_Company_Category,AboutCompanyCategoriesAdmin)
admin.site.register(Opportunities_category)
admin.site.register(Ourpartners_category)
admin.site.register(Ourpartners)
admin.site.register(AboutCompany)
admin.site.register(Oportunities)