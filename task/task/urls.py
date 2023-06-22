from django.contrib import admin
from django.urls import path
from app.views import *
from rest_framework.routers import DefaultRouter


# Создание экземпляра маршрутизатора
router = DefaultRouter()

# Регистрация маршрутов для категорий продуктов
router.register(r'product-categories', CategoryViewSet, basename='product-category')

# Регистрация маршрутов для групп продуктов
router.register(r'product-groups', GroupViewSet, basename='product-group')

# Регистрация маршрутов для продуктов
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Подключение маршрутов из маршрутизатора
    *router.urls,
]