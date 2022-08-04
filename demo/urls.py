from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('student-detail/<int:pk>/', views.studentDetail, name='student-detail'),
    path('student-create/', views.studentCreate, name='student-create'),
    path('student-update/<int:pk>/', views.studentUpdate, name='student-update'),
    path('student-delete/<int:pk>/', views.studentDelete, name='student-delete'),
]
