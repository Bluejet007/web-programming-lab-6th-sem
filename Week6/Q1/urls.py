from django.urls import path
from . import views

urlpatterns = [
    path('Q1/', views.Q1_view, name='Q1'),
    path('Q2/', views.Q2_view, name='Q2'),
    path('Q3/', views.Q3_view, name='Q3'),
    path('A1/', views.A1_view, name='A1')
]