# Generated by Django 5.0.6 on 2024-06-06 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=64, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tovars_images', verbose_name='IMG')),
                ('price', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Цена')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип')),
                ('shirina', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Ширина, см')),
                ('garant_srok', models.DecimalField(decimal_places=0, default=0, max_digits=3, verbose_name='Гарантийный срок')),
                ('glubina', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Глубина, см')),
                ('visote', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Высота, см')),
                ('opis_title', models.CharField(default='a', max_length=150, verbose_name='Описание название')),
                ('opis_dict', models.CharField(default='a', max_length=2500, verbose_name='Описание диск')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.categorii', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'Products',
            },
        ),
    ]
