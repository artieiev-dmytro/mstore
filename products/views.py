from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Categories, Product
from .serializers import CategoriesSerializer, ProductSerializer
from .filters import ProductFilter
from .pagination import CustomLimitOffsetPagination


class CategoriesAPIView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class DeteilCategoriesAPIView(generics.RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    pagination_class = CustomLimitOffsetPagination


class DeteilProductAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
