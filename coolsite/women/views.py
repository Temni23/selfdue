from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'women:about'},
    {'title': 'Добавить статью', 'url_name': 'women:add_page'},
    {'title': 'Обратная связь', 'url_name': 'women:contact'},
    {'title': 'Войти', 'url_name': 'women:login'}
]


def index(request):
    posts = Women.objects.all()
    template = 'women/index.html'
    cats = Category.objects.all()
    context = {'title': 'Главная страница',
               'menu': menu,
               'cats': cats,
               'posts': posts,
               'cat_selected': 0,}
    return render(request, template, context)


def show_post(request, post_id):
    post = get_object_or_404(Category,id=post_id)
    template = 'women/post.html'
    context = {'title': 'Главная страница',
               'menu': menu,
               'post': post}
    return render(request, template, context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    template = 'women/index.html'
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {'title': 'Главная страница',
               'menu': menu,
               'cats': cats,
               'posts': posts,
               'cat_selected': cat_id}
    return render(request, template, context)

def about(request):
    template = 'women/about.html'
    context = {'title': 'О сайте',
               'menu': menu}
    return render(request, template, context)


def addpage(request):
    return HttpResponse("Добавить статью")


def login(request):
    return HttpResponse("Авторизация")


def contact(request):
    return HttpResponse("Написать обращение")


def categories(request, slug):
    return HttpResponse(f'<h1>Заглушка намбер two</h1> {slug}')


def archive(request, year):
    if int(year) > 2023:
        return redirect('women:home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1> <p><h2>{year}</h2></p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>СТРАНИЦА НЕ НАЙДЕНА</h1>')
