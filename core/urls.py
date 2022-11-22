from django.urls import include, path
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
app_name = 'core'
router = DefaultRouter()
router.register('brands', views.BrandList, basename='brand_list')
router.register('content', views.ContentList, basename='content_list')
urlpatterns = router.urls

# urlpatterns = [
#     path("admin/", admin.site.urls),
#
# ]
