from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *


def main_page(request):
    posts = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
    else:
        form = SearchForm()
    return render(request, 'index.html', {'posts': posts, 'title': 'Каталог', 'form':form})


def show_product(request, product_id):
    post = Product.objects.get(pk=product_id)

    context = {'post': post, 'title': 'Каталог', 'product_id': product_id}
    return render(request, 'catalog.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = ShoppingCart.objects.filter(user=request.user, product=product_id)

    if not baskets.exists():
        ShoppingCart.objects.create(user=request.user, product=product, count=1)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.count += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, id):
    basket = ShoppingCart.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    form = ''
    str = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            str = form.cleaned_data["search"]

    else:
        form = SearchForm()

    sorts = Product.objects.filter(name__icontains=str)
    return render(request, 'search.html', context={"sorts" : sorts, "form":form})

