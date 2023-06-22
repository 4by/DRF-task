
import uuid
from django.db import models


class CategoriesOfProducts(models.Model):
    name = models.CharField(max_length=255, unique=True)
    seq = models.IntegerField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class GroupsOfProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_id = models.ForeignKey(
        CategoriesOfProducts, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_id = models.ForeignKey(GroupsOfProducts, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


# def create_test_data():
#     # Создание категорий, групп и продуктов
#     for i in range(1, 4):
#         category = CategoriesOfProducts.objects.create(
#             name=f"Category {i}", seq=i)

#         for j in range(1, 4):
#             group = GroupsOfProducts.objects.create(
#                 category_id=category, name=f"Group {j} in {category.name}", description=f"Description {j} in {category.name}", seq=j)

#             for k in range(1, 4):
#                 product = Products.objects.create(
#                     group_id=group, name=f"Product {k} in {group.name}", price=k * 10, hidden=False)

# Вызов функции для создания данных
# create_test_data()
