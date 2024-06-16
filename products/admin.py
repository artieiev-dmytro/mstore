from django.contrib import admin

from .models import Categories, Product


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)