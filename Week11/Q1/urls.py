from django.urls import path
from . import views

urlpatterns = [
    path('Q1/', views.Q1, name='Q1'),
    path('Q1/add-product/', views.Q1_product, name='Q1_product'),
    path('Q2/', views.Q2, name='Q2'),
    path('Q3/', views.Q3, name='Q3'),
    path('A1/', views.A1, name='A1')
]