from rest_framework import serializers
from .models import CategoriesOfProducts, GroupsOfProducts, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfProducts
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsOfProducts
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
