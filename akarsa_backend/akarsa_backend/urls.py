"""akarsa_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views as customer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("enter_otp/<pk>/",customer_views.enter_otp,name="customer_enter_otp"),
   
    path("dashboard/",customer_views.dashboard,name="customer_dashboard"),
    
    path("category/<pk>",customer_views.sub_category,name="subcategory"),
    path("concern/<pk>",customer_views.sub_concern,name="subconcern"),
    path("brand/<pk>",customer_views.sub_brand,name="subbrand"),
    # product description
    path("product_desc/<pk>/",customer_views.product_desc,name="product_desc"),
   
    path("ingrediant/<pk>",customer_views.sub_ingrediant,name="subingrediant"),
    path("type/<pk>",customer_views.sub_type,name="subtype"),
    path("buy_product/<int:pk>/",customer_views.buy_product,name="buy_product"),
    path("sub_cattegory_product/<pk>/",customer_views.sub_cattegory_product,name="sub_cattegory_product"),
    path("sub_concern_product/<pk>/",customer_views.sub_concern_product,name="sub_concern_product"),
    path("sub_ingrediant_product/<pk>/",customer_views.sub_ingrediant_product,name="sub_ingrediant_product"),
    path("sub_type_product/<pk>/",customer_views.sub_type_product,name="sub_type_product"),
    path("sub_brand_product/<pk>/",customer_views.sub_brand_product,name="sub_brand_product"),
    path("get_category/",customer_views.category,name="category"),
    path("get_concern/",customer_views.concern,name="concern"),
    path("get_ingrediant/",customer_views.ingrediant,name="ingrediant"),
    path("get_type/",customer_views.type,name="type"),
    path("get_brand/",customer_views.brand,name="brand"),
    path("home/",customer_views.home,name="home"),
    #path("products_in_cart/<pk>/",customer_views.products_in_cart,name="products_in_cart"),
    #path("cart/<pk>/",customer_views.cart,name="cart"),
    path("payment/",customer_views.payment,name="payment"),
    path("add_to_cart/pk",customer_views.add_to_cart,name="add_to_cart"),
    path("choose_payment/",customer_views.choose_payment,name="choose_payment"),
    path("order_review/",customer_views.order_review,name="order_review"),
    path("logout/",customer_views.user_logout,name="logout"),
    path("shopping/<int:pk>/",customer_views.Shopping_order,name="shopping_order"),
    

   
]