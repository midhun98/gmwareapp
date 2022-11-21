from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from core import models
# Create your views here.

def list(request):
    return render(request, 'frontend/list.html')


def createBrand(request):
    market = models.MarketPlace.objects.all()
    zipcode = models.ZipCode.objects.all()
    context = {
        "market": market,
        "zipcode": zipcode
    }
    return render(request, 'frontend/create_brand.html', context)

# @csrf_exempt
# def deleteBrand(request,pk):
#     models.Brand.objects.filter(id=pk).delete()
#     return render(request, 'frontend/list.html')
