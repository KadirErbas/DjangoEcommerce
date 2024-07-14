from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from . import models
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm
from django.views.generic import CreateView


category_name_mapping = {
        "islemciler": "İşlemciler",
        "anakartlar": "Anakartlar",
        "ramler": "Ram",
        "ekran_kartlari": "Ekran Kartları",
        "bilgisayar_kasalari": "Bilgisayar Kasaları",
        "islemci_sogutucular": "İşlemci Soğutucular",
        "kasa_fanlari": "Kasa Fanları",
        "termal_macunlar": "Termal Macunlar",
        "klavyeler": "Klavyeler",
        "monitorler": "Monitörler",
        "mouseler": "Mouseler",
}
def home_view(request):

    category_context = {"category_name_mapping": category_name_mapping}
    return render(request, 'parts_of_computer_app/home.html', context=category_context)

# views.py
def about_us(request):
    return render(request, 'aboutUs.html')


def detay_view(request, id):
    product = models.Product.objects.get(id=id)
    product_dict = {"product": product}
    return render(request, 'parts_of_computer_app/urun-detaylari.html',context=product_dict)



def product_by_search(request):
    search_query = request.GET.get('ara', '')
    products = []

    if search_query:
        products = models.Product.objects.filter(Q(name__icontains=search_query))

    no_results = len(products) == 0

    context = {
        'products': products,
        'search_query': search_query,
        'no_results': no_results
    }
    return render(request, 'parts_of_computer_app/show_products.html', context)



def products_by_cost(request):
    order = request.GET.get('order', '')
    category_name = request.GET.get('category', '')

    products = models.Product.objects.all()
    
    if category_name:
        category_id = category_mapping.get(category_name)
        if category_id is not None:
            products = products.filter(category_id=category_id)

    if order == 'price_asc':
        products = products.order_by('price')
    elif order == 'price_desc':
        products = products.order_by('-price')

    context = {
        'products': products,
        'order': order,
        'category_name': category_name,
        "category_name_mapping": category_name_mapping

    }
    return render(request, 'parts_of_computer_app/show_products.html', context)



    # Define a dictionary mapping category names to category IDs
category_mapping = {
        "islemciler": 1,
        "anakartlar": 2,
        "ramler": 3,
        "ekran_kartlari": 4,
        "bilgisayar_kasalari": 5,
        "islemci_sogutucular": 6,
        "kasa_fanlari": 7,
        "termal_macunlar": 8,
        "klavyeler": 9,
        "monitorler": 10,
        "mouseler": 11,
}

def getProductsByCategory(request, category):
    category_id = category_mapping.get(category)
    if category_id is not None:
        products = models.Product.objects.filter(category_id=category_id)
        template = 'parts_of_computer_app/show_products.html'
        context = {"products": products, "category_name": category, "category_name_mapping": category_name_mapping}
        return render(request, template, context)
    else:
        return HttpResponseNotFound("Kategori bulunamadı")

def getProductsByCategoryID(request, categoryID):
    category_list = list(category_mapping.keys())

    if (categoryID > len(category_list)):
        return HttpResponseNotFound('Kategori bulunamadı')

    category_name= category_list[categoryID-1]

    redirect_url = reverse('parts_of_computer_app:ProductsByCategory', args=[category_name])
    return redirect(redirect_url)   
    

@login_required(login_url="login")
def sepet_detay(request):
    return render(request, 'parts_of_computer_app/sepet_detay.html')

"""
def signup(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
"""

def signup(request):  
    if request.method == "POST":  
        form = CustomUserCreationForm(request.POST)  # Form verilerini burada işliyoruz
        if form.is_valid():  
            form.save()  
            return redirect('login')  # Başarılı kayıt sonrası yönlendirme

    else:  
        form = CustomUserCreationForm()  
    
    context = {  
        'form': form  
    }
    return render(request, 'registration/signup.html', context)

@login_required(login_url='login')
def add_to_cart(request, product_id):
    # Sepete ekleme işlemleri
    product = models.Product.objects.get(id=product_id)
    # Burada sepete ekleme işlemi yapılacak
    print(f"{product.name} başarıyla sepete eklendi.")
    return redirect('parts_of_computer_app:sepet_detay')

