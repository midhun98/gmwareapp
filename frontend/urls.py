from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('create-brand', views.createBrand, name="create_brand"),
    # path("delete-brand/<str:pk>", views.deleteBrand, name="delete_brand"),
]
