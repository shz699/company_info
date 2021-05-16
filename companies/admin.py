from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Business)
admin.site.register(Management)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(EmailFromUser)