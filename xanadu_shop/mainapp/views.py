from django.shortcuts import render

# Create your views here.

def main(request):

    return render(request, "mainapp/index.html")

def catalog_fullwidth(request):

    return render(request, "mainapp/catalog_fullwidth.html")

def about(request):

    return render(request, "mainapp/about.html")

