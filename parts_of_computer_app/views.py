from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . import models
from django.db.models import Q


# Create your views here.

def islemci_view(request):
    islemci = models.Product.objects.filter(category_id = 1)
    islemci_dict={"islemciler": islemci}
    return render(request, 'parts_of_computer_app/islemciler.html', context= islemci_dict)

def anakart_view(request):
    anakartlar = models.Product.objects.filter(category_id = 2)
    anakart_dict={"anakartlar":anakartlar}
    return render(request, 'parts_of_computer_app/anakartlar.html', context=anakart_dict)

def ram_view(request):
    ram = models.Product.objects.filter(category_id = 3)
    ram_dict={"ramler": ram}    
    return render(request, 'parts_of_computer_app/ramler.html', context= ram_dict)

def ekran_karti_view(request):
    ekran_karti = models.Product.objects.filter(category_id = 4)
    ekran_karti_dict={"ekran_kartlari": ekran_karti}       
    return render(request, 'parts_of_computer_app/ekran_kartlari.html',context=ekran_karti_dict)


def bilgisayar_kasalari_view(request):  
    bilgisayar_kasalari = models.Product.objects.filter(category_id = 5)
    bilgisayar_kasalari_dict={"bilgisayar_kasalari": bilgisayar_kasalari}   
    return render(request, 'parts_of_computer_app/bilgisayar_kasalari.html',context=bilgisayar_kasalari_dict)


def islemci_sogutucular_view(request):
    sogutucu = models.Product.objects.filter(category_id = 6)
    sogutucu_dict={"islemci_sogutucular": sogutucu}    
    return render(request, 'parts_of_computer_app/islemci_sogutucular.html', context= sogutucu_dict)

def kasa_fanlari_view(request):
    kasa_fanlari = models.Product.objects.filter(category_id = 7)
    kasa_fanlari_dict={"kasa_fanlari": kasa_fanlari}    
    return render(request, 'parts_of_computer_app/kasa_fanlari.html', context= kasa_fanlari_dict)

def termal_macun_view(request):
    termal_macun = models.Product.objects.filter(category_id = 8)
    termal_macun_dict={"termal_macunlar": termal_macun}    
    return render(request, 'parts_of_computer_app/termal_macunlar.html', context= termal_macun_dict)

def klavye_view(request):
    klavyeler = models.Product.objects.filter(category_id = 9)
    klavyeler_dict={"klavyeler": klavyeler}    
    return render(request, 'parts_of_computer_app/klavyeler.html', context= klavyeler_dict)

def monitor_view(request):
    monitorler = models.Product.objects.filter(category_id = 10)
    monitorler_dict={"monitorler": monitorler}    
    return render(request, 'parts_of_computer_app/monitorler.html', context= monitorler_dict)

def mouse_view(request):
    mouse = models.Product.objects.filter(category_id = 11)
    mouse_dict={"mouseler": mouse}    
    return render(request, 'parts_of_computer_app/mouseler.html', context= mouse_dict)

def home_view(request):
  
    products = models.Product.objects.all()
    products_dict = {"products": products}
    return render(request, 'parts_of_computer_app/home.html',context=products_dict)

def detay_view(request, id):
    
    product = models.Product.objects.get(id=id)
    print(product.category.name)

    product_dict = {"product": product}
    return render(request, 'parts_of_computer_app/urun-detaylari.html',context=product_dict)



def product_by_search(request):
    search_query = request.GET.get('search', '')
    products = []

    if search_query:
        products = models.Product.objects.filter(Q(name__icontains=search_query))

    no_results = len(products) == 0

    context = {
        'products': products,
        'search_query': search_query,
        'no_results': no_results
    }
    return render(request, 'parts_of_computer_app/home.html', context)



def products_by_cost(request):
    order = request.GET.get('order', '')
    category_name = request.GET.get('category', '')
    print("burası",order)
    print("burası",category_name)

    # Tüm ürünleri listeleyin, ardından kategoriye göre filtreleyin
    products = models.Product.objects.all()

    if category_name:
        products = products.filter(category__name=category_name)

    if order == 'price_asc':
        products = products.order_by('price')
    elif order == 'price_desc':
        products = products.order_by('-price')

    # Şablon adını dinamik olarak belirlemek
    if category_name:
        template_name = f'parts_of_computer_app/{category_name}.html'
        print(template_name)
    else:
        template_name = 'parts_of_computer_app/home.html'

    # category_name =  category_name.replace("-", "_")
    print("category",category_name)
    context = {
        category_name: products,  
        'order': order,
        'category': category_name
    }
    return render(request, template_name, context)


