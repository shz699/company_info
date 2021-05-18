from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from .forms import CreateCompany , CreateBusiness, EmailUser , CreateManagement
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    queryset =  EmailUser ()
    if request.method == 'POST':
        # queryset = EmailUser(request.POST)
        if queryset.is_valid:          
            email = request.POST['email']
            email_user = EmailFromUser(email=email)
            email_user.save()
    context = {
        'form' : queryset
    }
    return render(request , 'landing.html' , context)

@login_required
def CompanyList(request):
    queryset = Company.objects.all() 
    queryset_count = queryset.count()
    user = request.user
    queryset_user_count = queryset.filter(user=user).count()
    context = {
        'companies' : queryset , 
        'companies_count' : queryset_count ,
        'compaines_user_count' : queryset_user_count,
    }
    return render(request , 'companies/company_list.html' , context)


class CompanyCreateView(LoginRequiredMixin ,generic.CreateView):
    template_name = 'companies/company_create.html'
    form_class = CreateCompany
    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView , self).get_context_data(**kwargs)
        buss_form = CreateBusiness ()
        mang_form = CreateManagement ()
        all_company = Company.objects.all()
        context.update({
             'buss_form' : buss_form,
             'mang_form' : mang_form,
             'companies' : all_company,
        }) 
        return context
    
    def get_success_url(self):
        return reverse('companies:list')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super(CompanyCreateView , self).form_valid(form)  

def CompanyCreate(request):
    form = CreateCompany ()
    buss_form = CreateBusiness ()
    mang_form = CreateManagement ()
    all_company = Company.objects.all()
    if request.method == 'POST':
        form = CreateCompany (request.POST , request.FILES)
        if form.is_valid:
            form.save()
    context = {
        'form' : form,
        'buss_form' : buss_form,
        'mang_form' : mang_form,
        'companies' : all_company,
    }
    return render(request , 'companies/company_create.html' , context)


def bg(request):
    if request.method == 'POST':
        bg_form = CreateBusiness(request.POST or None)
        if bg_form is not None:
            bg_name = request.POST['bg_name']
            bg_model = Business(bg_name=bg_name)
            bg_model.save()   
        return redirect('/companies/create/')

def mng(request):
    if request.method == 'POST':
        mng_form = CreateManagement(request.POST or None)
        if mng_form is not None:
            mng_name = request.POST['mng_name']
            mng_model = Management(mng_name=mng_name)
            mng_model.save()

        return redirect('/companies/create/')


class CompanyDetailView(LoginRequiredMixin ,generic.DetailView):
    template_name = 'companies/company_detail.html'
    queryset = Company.objects.all()
    

class CompanyUpdateView(LoginRequiredMixin , generic.UpdateView):
    template_name = 'companies/company_update.html'
    form_class = CreateCompany
    queryset = Company.objects.all()

    def get_success_url(self):
        return reverse('companies:list')

class CompanyDeleteView(LoginRequiredMixin , generic.DeleteView):
    template_name = 'companies/company_delete.html'
    queryset = Company.objects.all()

    def get_success_url(self):
        return reverse('companies:list')
