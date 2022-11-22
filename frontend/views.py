from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from core import models


# Create your views here.

def list(request):
    brand = models.Brand.objects.all()
    market = models.MarketPlace.objects.all()
    zipcode = models.ZipCode.objects.all()
    context = {
        "brand": brand,
        "market": market,
        "zipcode": zipcode,
    }
    return render(request, 'frontend/list.html', context)


def createBrand(request):
    market = models.MarketPlace.objects.all()
    zipcode = models.ZipCode.objects.all()
    context = {
        "market": market,
        "zipcode": zipcode
    }
    if request.POST:
        name = request.POST.get('name')
        market = request.POST.get('market')
        zip = request.POST.get('zip')
        image = request.POST.get('image')
        models.Brand.objects.create(name=name,
                                    market_place=models.MarketPlace.objects.get(id=market),
                                    zip_code=models.ZipCode.objects.get(id=zip),
                                    image=image)
    return render(request, 'frontend/create_brand.html', context)


@csrf_exempt
def updateBrand(request, pk):
    name = request.POST['name']
    market = request.POST['market']
    zip = request.POST['zip']

    print(name, market, zip)
    models.Brand.objects.filter(id=pk).update(name=name, market_place=market, zip_code=zip)
    return render(request, 'frontend/list.html')


def contentList(request):
    return render(request, 'frontend/content_list.html')
