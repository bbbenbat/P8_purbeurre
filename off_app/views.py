import operator
from functools import reduce

from django.db.models import Q
from django.shortcuts import render, redirect

from off_app.favorite import FavoriteForm
from off_app.models import Product

def main_page(request):
    return render(request, 'index.html')

"""def research_product(request):
    products = Product.objects.all()
    return render(request, 'research_product.html', {'product': products})"""




def create_favorite(request):
    if request.method == "GET":
        form = FavoriteForm()
        return render(request, 'addfavorite.html', locals())
    elif request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save()
            return redirect('research_product')



