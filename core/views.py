from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, serializers


# Create your views here.

class BrandList(ModelViewSet):
    serializer_class = serializers.BrandSerializer
    queryset = models.Brand.objects.all()

    # get a brand based on pk, method - GET
    def retrieve(self, request, *args, **kwargs):
        print('retrieve')
        pk = kwargs.get('pk')
        try:
            brand = models.Brand.objects.get(id=pk)
        except:
            return Response('Brand doesnt exist')
        serializer = serializers.BrandSerializer(brand, many=False)
        return Response({"Message": 'Brand Retrieved', "data": serializer.data})

    # create a new brand, method - POST
    def create(self, request, *args, **kwargs):
        print('create')
        serializer = serializers.BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"Message": 'Brand Created', "data": serializer.data})

    # update a brand based on primary key and passed data, method - PATCH
    def update(self, request, *args, **kwargs):
        print('update')
        pk = kwargs.get('pk')
        try:
            brand = models.Brand.objects.get(id=pk)
        except:
            return Response('Brand doesnt exist')
        serializer = serializers.BrandSerializer(instance=brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"Message": 'Brand Updated', "data": serializer.data})

    # delete a brand based on the passed pk, method - DELETE
    def destroy(self, request, *args, **kwargs):
        print("destroy")
        pk = kwargs.get('pk')
        try:
            brand = models.Brand.objects.get(id=pk)
        except:
            return Response('Brand doesnt exist')
        brand.delete()
        return Response({"Message": 'Brand deleted'})


class ContentList(ModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer

    # get a content  based on pk, method - GET
    def retrieve(self, request, *args, **kwargs):
        print('content retrieve')
        pk = kwargs.get('pk')
        try:
            brand = models.Content.objects.get(id=pk)
        except:
            return Response('Content doesnt exist')
        serializer = self.serializer_class(brand, many=False)
        return Response({"Message": 'Content Retrieved', "data": serializer.data})

    # create a new content, method - POST
    def create(self, request, *args, **kwargs):
        print('content create')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": 'Content Created', "data": serializer.data})
        else:
            return Response({"Error": serializer.errors})

    # update a content based on primary key and passed data, method - PATCH
    def update(self, request, *args, **kwargs):
        print('content update')
        pk = kwargs.get('pk')
        print(pk)
        try:
            brand = models.Content.objects.get(id=pk)
        except:
            return Response('Content doesnt exist')
        serializer = self.serializer_class(instance=brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": 'Content Updated', "data": serializer.data})
        else:
            return Response({"Error": serializer.errors})


    # delete a content based on the passed pk, method - DELETE
    def destroy(self, request, *args, **kwargs):
        print("content destroy")
        pk = kwargs.get('pk')
        try:
            brand = models.Content.objects.get(id=pk)
        except:
            return Response('content doesnt exist')
        brand.delete()
        return Response({"Message": 'Content deleted'})
