from rest_framework import serializers
from . import models

class BrandSerializer(serializers.ModelSerializer):
    # market_place = serializers.CharField(source='market_place.name')
    # zip_code = serializers.CharField(source='zip_code.code')
    class Meta:
        model = models.Brand
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data)
    #     return models.Brand.objects.create(**validated_data)
