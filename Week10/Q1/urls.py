from django.urls import path
from . import views

urlpatterns = [
    path('Q1/', views.Q1, name='index'),
    path('Q1/add-category/', views.Q1_category, name='add_category'),
    path('Q1/add-page/', views.Q1_page, name='add_page'),
    path('Q2/add/', views.add_work, name='add_work'),
    path('Q2/search/', views.search_company, name='search_company'),
    path('A1/', views.A1, name='A1')
]