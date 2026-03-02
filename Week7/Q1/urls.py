from django.urls import path
from . import views

urlpatterns = [
    path('Q1/', views.Q1_view, name='Q1'),
    path('Q1/', views.Q1_res_view, name='Q1_res'),
    path('Q2/', views.Q2_view, name='Q2'),
    path('Q2_sec/', views.Q2_sec_view, name='Q2_sec'),
    path('A1/', views.A1_view, name='A1')
]