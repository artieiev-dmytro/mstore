from rest_framework import serializers

from .models import Categories, Product


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("id", "name", "image")


class ProductSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()

    class Meta:
        model = Product
        fields = '__all__'
