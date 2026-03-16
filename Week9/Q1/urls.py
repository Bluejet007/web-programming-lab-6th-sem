from django.urls import path
from . import views

urlpatterns = [
    path('Q1/', views.Q1_reg_view, name='Q1'),
    path('Q2/', views.Q2_view, name='Q2'),
    path('Q3/', views.Q3_view, name='Q3'),
    path('Q3_res/', views.Q3_res_view, name='Q3_res'),
    path('A1/', views.A1_view, name='A1'),
    path('A2/', views.A2_view, name='A2')
]