from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    bg_name = models.CharField(max_length=50)

    def __str__(self):
        return self.bg_name

    class Meta:
        verbose_name_plural = 'Businesses' 

class Management(models.Model):
    mng_name = models.CharField(max_length=50)    

    def __str__(self):
        return self.mng_name

class Country(models.Model):
    name = models.CharField(max_length=50)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'    

class City(models.Model):
    country = models.ForeignKey('Country' , on_delete=models.CASCADE)   
    # country = models.ForeignKey('Country' ,blank=True , null=True , on_delete=models.SET_NULL)   
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'      

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company' , default='logo.png' , null=True)
    # business_type = models.ForeignKey('Business',blank=True , null=True  , on_delete=models.SET_NULL)
    business_type = models.ForeignKey('Business', on_delete=models.CASCADE)
    # management_type = models.ForeignKey('management' ,blank=True , null=True , on_delete=models.SET_NULL)
    management_type = models.ForeignKey('management', on_delete=models.CASCADE)
    incorporation_date = models.DateTimeField(default=now)
    # updated = models.DateTimeField(auto_now=True)
    incorporation_no = models.CharField(max_length=200)
    registered_address = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    # country = models.ForeignKey('Country' ,blank=True , null=True , on_delete=models.SET_NULL)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    # city = models.ForeignKey('City' ,blank=True , null=True , on_delete=models.SET_NULL)
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.company_name}" 
        # return f"{self.company_name} was created on {self.incorporation_date.strftime('%d/%m/%Y')}" 


class EmailFromUser(models.Model):
    email = models.EmailField(max_length=254)   
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} | created on {self.created}'

