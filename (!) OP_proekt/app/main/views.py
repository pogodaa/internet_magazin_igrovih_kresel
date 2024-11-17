from django.shortcuts import get_list_or_404, render

from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render,get_object_or_404

from main.utilits import q_search
from .models import Products, Categorii


def index(request):
      category = Categorii.objects.all()
      tovars = Products.objects.all()

      context = {
            'category': category,
            'tovars':tovars,
      }

      return render(request, 'main/face.html', context)


# Страница категории
def catalog_page(request, catalog_slug=None):

      page = request.GET.get("page", 1)
      order_by = request.GET.get("order_by", None)
      querry = request.GET.get("q", None)

      if catalog_slug == 'vse-tovary':
            tovars = Products.objects.all()

      elif querry:
            tovars = q_search(querry)
      else:
            tovars = get_list_or_404(Products.objects.filter(category__slug=catalog_slug))

      if order_by and order_by !='default':
            tovars = tovars.order_by(order_by)

      paginator = Paginator(tovars, 9)
      current_page = paginator.page(int(page))

      category = Categorii.objects.all()

      context = {

            'category': category,

            'tovars':current_page,

            'slug_url':catalog_slug,
      }

      return render(request, 'main\index.html', context)


# Страница продукта
def product_page(request, product_slug):

      category = Categorii.objects.all()

      product = Products.objects.get(slug=product_slug)

      context = {
            'product': product,
            'category': category,
      }

      return render(request, 'main\covars\se_for_otdelno_tovar.html', context)


def login_autoriz(request):
      return render(request, 'main\login.html')

def politica_konf(request):

      category = Categorii.objects.all()

      context = {
            'category': category,
      }

      return render(request, 'main\huter\politica.html', context)

def sogl_obrabotka_pes_dannix(request):

      category = Categorii.objects.all()

      context = {
         
            'category': category,
      }

      return render(request, 'main\huter\sogl.html', context)

def about_page(request):

      category = Categorii.objects.all()

      context = {
            'category': category,
      }

      return render(request, 'main\huter\page.html', context)

def dostavka_oplata(request):
      
      category = Categorii.objects.all()

      context = {
            'category': category,
      }
      
      return render(request, 'main\huter\dos_op.html', context)

def kontakti_page(request):
      
      category = Categorii.objects.all()

      context = {
            'category': category,
      }

      return render(request, 'main\huter\kontakti.html', context)
