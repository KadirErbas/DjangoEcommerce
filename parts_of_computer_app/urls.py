from django.urls import path
from . import views

app_name = 'parts_of_computer_app'

urlpatterns = [
    path("", views.home_view, name="home"),

    path('signup/', views.signup, name="signup"), # tamamlanmadı

    path('ara/', views.product_by_search, name='product_by_search'),
    
    path("<int:categoryID>", views.getProductsByCategoryID),
    path("<str:category>", views.getProductsByCategory, name="ProductsByCategory"),


    path("urun-detaylari/<int:id>/", views.detay_view, name="urun-detaylari"),
  
    path("sort/", views.products_by_cost, name="products_by_cost"),     

    path('about-us/', views.about_us, name="about_us"),


    path('sepet/', views.sepet_detay, name='sepet_detay'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


]