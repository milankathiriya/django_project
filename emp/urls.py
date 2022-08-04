from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('', views.EmployeeViewSet, basename='home')

urlpatterns = [
    # path('', views.EmployeeList.as_view()),
    # path('<int:pk>/', views.EmployeeDetail.as_view()),
]


urlpatterns = router.urls