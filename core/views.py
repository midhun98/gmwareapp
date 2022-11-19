from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers
from django.shortcuts import get_object_or_404
# Create your views here.

class BrandList(viewsets.ViewSet):
    queryset = models.Brand.objects.all()

    def list(self, request):
        serializer_class = serializers.BrandSerializer(self.queryset, many=True)
        print(serializer_class.data)
        return Response(serializer_class.data)

    def details(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk)
        serializer_class = serializers.BrandSerializer(post)
        return Response(serializer_class.data)

    def update
