from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/home.html', {'title': 'Home'})


# Функция render()
# принимает объект запроса в качестве первого аргумента,
# имя шаблона (templates = 'main/home.html') в качестве второго аргумента
# и словарь в качестве необязательного третьего аргумента.
# Она возвращает объект HttpResponse данного шаблона, отображенный в данном контексте.

# Другими словами:
# Функция home вызывает функцию render, которой передаются объект запроса request
# и путь к файлу шаблона в рамках папки templates - 'main/home.html'.
