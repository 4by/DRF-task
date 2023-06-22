import copy

from django.db.models import Max
from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import CategoriesOfProducts, GroupsOfProducts, Products
from .serializers import CategorySerializer, GroupSerializer, ProductSerializer

# Класс пагинации с значениями по умолчанию


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100

# Представление для категорий продуктов


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = CategoriesOfProducts.objects.all().order_by('seq')
        category_id = self.request.query_params.get('categories_id')
        return queryset.filter(id=category_id) if category_id else queryset

    def create(self, request, *args, **kwargs):
        seq = request.data.get('seq')

        if not seq:
            max_seq = CategoriesOfProducts.objects.all().aggregate(Max('seq'))[
                'seq__max']
            seq = max_seq + 1 if max_seq is not None else 1

        request.data._mutable = True
        request.data['seq'] = seq
        request.data._mutable = False

        return super().create(request, *args, **kwargs)


# Представление для групп продуктов
class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = GroupsOfProducts.objects.all().order_by('seq')
        category_id = self.request.query_params.get('categories_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def create(self, request, *args, **kwargs):
        category_id = request.data.get('category_id')
        seq = request.data.get('seq')

        if not seq:
            max_seq = GroupsOfProducts.objects.filter(
                category_id=category_id).aggregate(Max('seq'))['seq__max']
            seq = max_seq + 1 if max_seq is not None else 1

        request.data._mutable = True
        request.data['seq'] = seq
        request.data._mutable = False

        return super().create(request, *args, **kwargs)


# Представление для продуктов
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = Products.objects.all().order_by('price')

        search_by_name = self.request.query_params.get('search_by_name')
        group_id = self.request.query_params.get('group_id')

        if search_by_name:
            queryset = queryset.filter(name__icontains=search_by_name)

        if group_id:
            queryset = queryset.filter(group_id=group_id)

        return queryset
