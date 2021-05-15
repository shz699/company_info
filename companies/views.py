from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from .forms import CreateCompany , CreateBusiness ,CreateManagement
from django.views import generic

# Create your views here.
def landing(request):
    return render(request , 'landing.html')

def CompanyList(request):
    queryset = Company.objects.all()
    context = {
        'companies' : queryset
    }
    return render(request , 'companies/company_list.html' , context)


class CompanyCreateView(generic.CreateView):
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
        print(form) 
        form.save()
        return super(CompanyCreateView , self).form_valid(form)  

def CompanyCreate(request):
    form = CreateCompany ()
    buss_form = CreateBusiness ()
    mang_form = CreateManagement ()
    if request.method == 'POST':
        form = CreateCompany (request.POST or None)
        if form is not None:
            f = request.POST['company_name']
            print(f)    
    context = {
        'form' : form,
        'buss_form' : buss_form,
        'mang_form' : mang_form,
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


class CompanyDetailView(generic.DetailView):
    template_name = 'companies/company_detail.html'
    queryset = Company.objects.all()

class CompanyUpdateView(generic.UpdateView):
    template_name = 'companies/company_update.html'
    form_class = CreateCompany
    queryset = Company.objects.all()

    def get_success_url(self):
        return reverse('companies:list')

class CompanyDeleteView(generic.DeleteView):
    template_name = 'companies/company_delete.html'
    queryset = Company.objects.all()

    def get_success_url(self):
        return reverse('companies:list')