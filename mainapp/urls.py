from mainapp.models import Product
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='catalog'),
    path('<int:id>', mainapp.catalog, name='catalog'),
]
