from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Car

# Create your views here.

def list_cars(request: HttpRequest) -> HttpResponse:
    return render(request, 'cars/list_cars.html', {'cars': Car.objects.all()})

def detail_car(request: HttpRequest, car_id: int) -> HttpResponse:
    return render(request, 'cars/car_detail.html', {'car': Car.objects.get(id=car_id)})



# Функция render()
# принимает объект запроса в качестве первого аргумента,
# имя шаблона (templates = 'cars/list_cars.html') в качестве второго аргумента
# и словарь в качестве 'необязательного' третьего аргумента.
# Она возвращает объект HttpResponse данного шаблона, отображенный в данном контексте.

# Другими словами:
# Функция home вызывает функцию render, которой передаются объект запроса request
# и путь к файлу шаблона в рамках папки templates - 'main/home.html'.