from django.contrib import admin
from .models import StudentHelpInformation,\
    AboutUs,\
    Contacts,\
    AbiturientHelpInformation, Ourpartners,AboutCompany,Oportunities
# Register your models here.


admin.site.register(StudentHelpInformation)
admin.site.register(AbiturientHelpInformation)
admin.site.register(AboutUs)
admin.site.register(Contacts)
admin.site.register(Ourpartners)
admin.site.register(AboutCompany)
admin.site.register(Oportunities)