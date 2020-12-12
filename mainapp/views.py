from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from .models import Brand, Package, Classification, Country, Strong, Style, Product


def main(request):

    content = {
        'title': 'main'
    }

    return render(request, 'mainapp/index.html', content)


def catalog(request):

    start = 1
    finish = 15
    count = 15

    products = Product.objects.all()[start-1:finish-1]

    content = {
        'title': 'catalog',
        'products': products,
        'start': start,
        'finish': finish,
        'count': count
    }

    return render(request, 'mainapp/catalog.html', content)


def about(request):

    content = {
        'title': 'about',
    }

    return render(request, 'mainapp/about.html', content)
