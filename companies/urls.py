from django.urls import path 
from . import views
from .views import CompanyCreateView , CompanyDetailView , CompanyUpdateView , CompanyDeleteView

app_name='companies'

urlpatterns = [
    path('list/', views.CompanyList , name='list'),
    # path('create/', views.CompanyCreate , name='create'),
    path('create/', views.CompanyCreateView.as_view() , name='create'),
    path('<int:pk>/', views.CompanyDetailView.as_view() , name='detail'),
    path('<int:pk>/update/', views.CompanyUpdateView.as_view() , name='update'),
    path('<int:pk>/delete/', views.CompanyDeleteView.as_view() , name='delete'),
    path('create/bg/', views.bg , name='bg'),
    path('create/mng/', views.mng , name='mng'),
]