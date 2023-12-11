from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_cars, name='home'),
    path('car_detail/<int:car_id>/', views.detail_car, name='detail'),
]