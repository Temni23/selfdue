from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Women.objects.all()
    template = 'women/index.html'
    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts}
    return render(request, template, context)


def about(request):
    template = 'women/about.html'
    context = {'title': 'О сайте',
               'menu': menu}
    return render(request, template, context)


def categories(request, slug):
    return HttpResponse(f'<h1>Заглушка намбер two</h1> {slug}')


def archive(request, year):
    if int(year) > 2023:
        return redirect('women:home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1> <p><h2>{year}</h2></p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>СТРАНИЦА НЕ НАЙДЕНА</h1>')
