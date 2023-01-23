"""Time2Play URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Time2Playapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage),
    path('login/registo/', views.popularUser),
    path('login/', views.login),

    path('c1/', views.c1),
    path('c1/addPrdt/', views.addPrdt),
    path('c1/listPrdt/', views.listPrdt),
    path('c1/listPrdt/deleteprdt/<int:ProductId>/', views.deletePrdt),
    path('c1/sales/', views.addSale),
    path('c1/removeSales/', views.removeSale),
    path('c1/partnerPrdt/', views.listPartnerPrdt),
    path('c1/listPrdt/partnerPrdt/AlterarStatusProduto/<int:ProductId>/', views.ChangePrdtStatus),
    path('c1/chart/', views.count_products),
    path('c1/listclient/', views.list_cliente),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
