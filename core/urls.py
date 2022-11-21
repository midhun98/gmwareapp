from django.urls import include, path
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
app_name = 'core'
router = DefaultRouter()
router.register('', views.BrandList, basename='brand_list')
urlpatterns = router.urls

# urlpatterns = [
#     path("admin/", admin.site.urls),
#
# ]
