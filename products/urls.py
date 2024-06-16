from django.urls import path

from .views import CategoriesAPIView, DeteilCategoriesAPIView, ProductsAPIView, DeteilProductAPIView

app_name = 'products'


urlpatterns = [
    path("products/", ProductsAPIView.as_view(), name="products"),
    path("products/<int:pk>", DeteilProductAPIView.as_view(), name="product"),
    path("categories/", CategoriesAPIView.as_view(), name="categories"),
    path("categories/<int:pk>", DeteilCategoriesAPIView.as_view(), name="category"),
]
