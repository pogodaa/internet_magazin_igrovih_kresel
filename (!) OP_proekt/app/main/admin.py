from django.contrib import admin

# Register your models here.
from main.models import Categorii, Products

# Register your models here.

# admin.site.register(Categorii)
# admin.site.register(Products)

@admin.register(Categorii)
class CategoriiAdmin(admin.ModelAdmin):
      prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
      prepopulated_fields = {'slug': ('name',)}