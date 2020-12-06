from django.shortcuts import render

product_simple = {
    "title":"Bouble Fabric Blazer",
    "img":"assets/images/products/featured/1.jpg",
    "old_price":"700.00",
    "price":"69.90",
    "description":"Dramatically transition excellent information rather than mission-critical results. Competently communicate fully tested core competencies through holistic resources. Professionally maintain high-payoff best practices whereas user-centric alignments. Intrinsicly engage future-proof best practices whereas economically sound resources. Holisticly maximize multidisciplinary synergy before magnetice-tailers."
}

product_simple_list = [product_simple for inx in range(15)]

def main(request):

    content = {
        "title": "main"
    }

    return render(request, 'mainapp/index.html',content)

def catalog(request):

    content = {
        "title": "catalog",
        "products": product_simple_list,
        "start":1,
        "finish":15,
        "count":15
    }

    return render(request, 'mainapp/catalog.html',content)

def about(request):

    content = {
        "title": "about",
    }

    return render(request, 'mainapp/about.html',content)

