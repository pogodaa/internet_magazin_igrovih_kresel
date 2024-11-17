from django.db import models


# Create your models here.




# TOVARS
from django.db import models

# Create your models here.

# id создаётся автоматически

# class Categorii(models.Model):
#       name = models.CharField(max_length=32, unique=True, verbose_name='Название')

#       # Фрагмент текстового url адреса который будет вести на соответствующую категорию (текстовый URL-адрес категории.)
#       slug = models.SlugField(max_length=64, unique=True, blank=True, null=True, verbose_name='URL')

#       class Meta:
#             # Название дл БД
#             db_table = 'Category'

#             # Название для admin
#             verbose_name = 'Категорию'

#             # Во множественном числе
#             verbose_name_plural = 'Категории'
      
#       def __str__(self):
#             return self.name

# class Products(models.Model):
#       name = models.CharField(max_length=150, unique=True, verbose_name='Название')
#       slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
#       image = models.ImageField(upload_to='tovars_images' ,blank=True, null=True, verbose_name='IMG')
#       price = models.DecimalField(max_digits=15, decimal_places=0 , verbose_name='Цена')

#       type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип')
#       shirina = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Ширина, см')
#       garant_srok = models.DecimalField(default=0, max_digits=3, decimal_places=0  ,verbose_name='Гарантийный срок')
#       glubina = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Глубина, см')
#       visote = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Высота, см')

#       opis_title = models.CharField(default='a', max_length=150, verbose_name='Описание название')
#       opis_dict = models.CharField(default='a', max_length=2500, verbose_name='Описание диск')

#       category = models.ForeignKey(to=Categorii, on_delete=models.PROTECT, verbose_name='Категория')

#       class Meta:
#             # Название дл БД
#             db_table = 'Products'

#             # Название для admin
#             verbose_name = 'Продукт'

#             # Во множественном числе
#             verbose_name_plural = 'Продукты'

#       def __str__(self):
#             return self.name
      
#       # def display_id(self):
#       #       return f'{self.id:04}'