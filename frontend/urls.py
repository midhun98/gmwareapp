from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('create-brand', views.createBrand, name="create_brand"),
    path("update-brand/<str:pk>", views.updateBrand, name="update-brand"),
    path("content-list", views.contentList, name="content-list"),
    path("create-content", views.createContent, name="create-content"),
]
