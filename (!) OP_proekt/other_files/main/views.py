from django.shortcuts import render


# Create your views here.
def index(request):
      return render(request, 'main\index.html')

def login_autoriz(request):
      return render(request, 'main\login.html')

def politica_konf(request):
      return render(request, 'main\politica.html')

def sogl_obrabotka_pes_dannix(request):
      return render(request, 'main\sogl.html')

def about_page(request):
      return render(request, 'main\page.html')

def dostavka_oplata(request):
      return render(request, 'main\dos_op.html')

def kontakti_page(request):
      return render(request, 'main\kontakti.html')

# Tovars
# from django.shortcuts import render

# from tovars.models import Products, Categorii

# Create your views here.

# Page Categoria


# Офисные
# def office_chairs(request):
#       return render(request, 'tovars\page_office_chairs.html')

# def category_page(request, category_slug):
      
#       if category_slug == 'vse-tovary':
#             tovars = Products.objects.all()
#       else:
#             tovars = Products.objects.filter(category__slug=category_slug)

#       context = {
#             'tovars': tovars,
#       }

#       return render(request, 'tovars\se_tovars.html', context=context)



# # Page tovar_single

# def product_page(request, product_slug):

#       product = Products.objects.get(slug=product_slug)

#       context = {
#             'product': product
#       }

#       return render(request, 'tovars\se_for_otdelno_tovar.html', context=context)
