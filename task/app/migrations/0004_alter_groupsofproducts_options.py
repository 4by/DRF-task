# Generated by Django 4.2.2 on 2023-06-19 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_categorysd_groupsofproducts_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupsofproducts',
            options={'verbose_name': 'группа', 'verbose_name_plural': 'группы'},
        ),
    ]
