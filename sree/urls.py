"""sree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('home',views.home,name="home"),
    path('shop',views.s,name="s"),
    path('buy/<int:id>/',views.buy,name="buy"),
    path('form',views.add,name="addd"),
    path('biling/<int:id>/',views.biling,name="bilingg"),
    path('rs',views.rs,name="rs"),
    path('register/',views.register,name="r"),
    path('muorder',views.myorder,name="myorder"),
    path('vegetables/', views.vegetable_list, name='vegetable_list'),
    path('make_offer/<int:vegetable_id>/', views.make_offer, name='make_offer'),
    path('ovl',views.ovl,name="ovl"),
    path('ovl/<int:id>/',views.accept_offer,name="accept_offer"),
    path('add/', views.add_insurance, name='add'),
    path('te/',views.weather_view,name="wheather"),
    path('ins_list', views.insurance_list, name='ins_list'),
    path('shopl',views.shop_list,name="shop_list"),
    path('addsh',views.add_shop,name="add_shop"),
    path('loan/application/', views.loan_application, name='loan_application'),
    path('loan/list/', views.loan_list, name='loan_list'),
    path('contact',views.submit,name="submit"),
    path('ad',views.admin_ll,name="al"),
    path('ad_pa',views.admin_home,name="ad_ho"),
    path('co',views.contact_details,name="contacts"),
    path('or_ca/<int:id>/',views.or_ca,name="or_ca"),
    path('or',views.orderss,name="orderss"),
]
