from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('vacancies/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancies/create/', views.vacancy_create, name='vacancy_create'),
    path('vacancies/update/<int:pk>/', views.vacancy_update, name='vacancy_update'),
    path('vacancies/delete/<int:pk>/', views.vacancy_delete, name='vacancy_delete'),
    path('resumes/', views.resume_list, name='resume_list'),
    path('resumes/<int:pk>/', views.resume_detail, name='resume_detail'),
    path('resumes/create/', views.resume_create, name='resume_create'),
    path('resumes/update/<int:pk>/', views.resume_update, name='resume_update'),
    path('resumes/delete/<int:pk>/', views.resume_delete, name='resume_delete'),
]
