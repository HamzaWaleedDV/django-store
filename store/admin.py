from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryModel(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Author)
class AuthorModel(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Product)
class ProductModel(admin.ModelAdmin):
    list_per_page = 20    



@admin.register(models.Slider)
class SliderModel(admin.ModelAdmin):
    list_per_page = 20