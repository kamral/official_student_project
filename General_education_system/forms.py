from django import forms
from .models import General_education_system,Category_education


class General_education_systemForm(forms.ModelForm):

    class Meta:
        model=General_education_system
        fields=['image','name','address','category',
               'filial','history_of_university']
