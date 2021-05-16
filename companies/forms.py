from django import forms
from django.forms import models
from .models import Company , Business , Management , EmailFromUser

class CreateCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'company_name',
            'logo',
            'business_type',
            'management_type',
            'incorporation_date',
            'incorporation_no',
            'registered_address',
            'country',
            'city',
        )

class CreateBusiness(forms.ModelForm):
    class Meta:
        model = Business
        fields = (
            'bg_name',
        )
class CreateManagement(forms.ModelForm):
    class Meta:
        model = Management
        fields = (
            'mng_name',
        )

class EmailUser(forms.ModelForm):
    class Meta:
        model = EmailFromUser
        fields = (
            'email',
        )

        
