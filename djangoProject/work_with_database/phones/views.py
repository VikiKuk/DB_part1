from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):

    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'min_price':
        sort_by = f'price'
    elif sort_by == 'max_price':
        sort_by = f'-price'
    catolog_info = Phone.objects.order_by(sort_by).values('id','name', 'price', 'image', 'slug')
    context = {'phones': catolog_info}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.filter(slug=slug).first()
    context = {'phone': product}
    return render(request, template, context)



