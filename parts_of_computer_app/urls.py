from django.urls import path
from . import views

app_name = 'parts_of_computer_app'

urlpatterns = [
    path("", views.home_view, name="home"),
    path("islemciler/", views.islemci_view, name="islemciler"),
    path("anakartlar/", views.anakart_view, name="anakartlar"),
    path("ramler/", views.ram_view, name="ramler"),
    path("ekran-kartlari/", views.ekran_karti_view, name="ekran_kartlari"),
    path("bilgisayar-kasalari/", views.bilgisayar_kasalari_view, name="bilgisayar_kasalari"),
    path("islemci-sogutucular/", views.islemci_sogutucular_view, name="islemci_sogutucular"),
    path("kasa-fanlari/", views.kasa_fanlari_view, name="kasa_fanlari"),
    path("termal-macunlar/", views.termal_macun_view, name="termal_macunlar"),
    path("klavyeler/", views.klavye_view, name="klavyeler"),
    path("monitorler/", views.monitor_view, name="monitorler"),
    path("mouseler/", views.mouse_view, name="mouseler"),

    path("urun-detaylari/<int:id>/", views.detay_view, name="urun-detaylari"),
  
    path("sort/", views.products_by_cost, name="product_by_cost"),




]