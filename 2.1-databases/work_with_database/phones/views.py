from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
##===================
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(SORT_MAP[sort])
    context = {'phones': phones}
    return render(request, template, context)
##============
    # phones_sort = request.GET.get('sort', '')
    # phones_all = Phone.objects.all()
    #
    # if phones_sort == 'name':
    #     phones = phones_all.order_by('name')
    #     context = {'phones': phones}
    #     return render(request, template, context)
    # elif phones_sort == 'max_price':
    #     phones = phones_all.order_by('-price')
    #     context = {'phones': phones}
    #     return render(request, template, context)
    # elif phones_sort == 'min_price':
    #     phones = phones_all.order_by('price')
    #     context = {'phones': phones}
    #     return render(request, template, context)

    context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
