from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    market_place = serializers.CharField(source='market_place.name', read_only=True)
    zip_code = serializers.CharField(source='zip_code.code', read_only=True)

    class Meta:
        model = models.Brand
        fields = '__all__'

    def create(self, validated_data):
        return models.Brand.objects.create(**validated_data)

#
# class ChannelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Channel
#         fields = '__all__'
#
#
# class MarketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.MarketPlace
#         fields = '__all__'
#
#
# class BrandsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Brand
#         fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    # channel = ChannelSerializer()

    class Meta:
        model = models.Content
        fields = '__all__'
        depth = 1