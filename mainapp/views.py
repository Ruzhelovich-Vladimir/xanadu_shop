from django.conf import settings
from django.core import paginator
from django.shortcuts import render
from django.utils import timezone

from mainapp.models import Brand, Package, Classification, Country, Strong, Style, Product

from django.core.paginator import Paginator


def main(request):

    content = {
        'title': 'main'
    }

    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):

    page_cnt = 15
    products = Product.objects.all()
    paginator = Paginator(products, page_cnt)

    content = {
        'title': 'catalog',
        'products': paginator
    }

    return render(request, 'mainapp/catalog.html', content)


def about(request):

    content = {
        'title': 'about',
    }

    return render(request, 'mainapp/about.html', content)
