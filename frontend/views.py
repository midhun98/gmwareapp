from django.shortcuts import render, redirect
from core import models
# Create your views here.

def list(request):
    return  render(request, 'frontend/list.html')

