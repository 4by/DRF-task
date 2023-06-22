from django.contrib import admin
from .models import CategoriesOfProducts, GroupsOfProducts, Products

class CategoriesOfProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'seq')

class GroupsOfProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category_id', 'description', 'seq')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'group_id', 'price', 'hidden')

admin.site.register(CategoriesOfProducts, CategoriesOfProductsAdmin)
admin.site.register(GroupsOfProducts, GroupsOfProductsAdmin)
admin.site.register(Products, ProductsAdmin)
