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
    path('addcartnouser/<int:id>/', views.addCartNoUser),
    path('cart/', views.cartNoUser),
    path('cart/login', views.cartNoUserLogin),
    path('filtros', views.categorias2),
    path('xbox', views.xbox_list2),
    path('pc', views.pc_list2),
    path('nintendo', views.nintendo_list2),
    path('playstation', views.playstation_list2),

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
    path('c1/listorders/', views.list_orders),
    path('c1/pedirproc',views.listxml),
    path('c1/pedirproclist',views.pedirproc),
    path('c1/listorders/filtrar/<str:data>/', views.list_orders_filter),
    path('c1/partnerPrdt/partnerPrdt/AlterarStatusProduto/<int:ProductId>/', views.ChangePrdtStatus),

    path('c2/', views.c2),
    path('c2/listPrdt/', views.listPrdt2),
    path('c2/sales/', views.addSale2),
    path('c2/removeSales/', views.removeSale),
    path('c2/pedirproc',views.listxml),
    path('c2/pedirproclist2',views.pedirproc),
    path('c2/listorders2/', views.list_orders2),
    path('c2/listorders2/filtrar/<str:data>/', views.list_orders_filter2),

    path('adm/',views.adm),
    path('adm/aprpar',views.aprpar),
    path('adm/criarut',views.criarut),
    path('adm/gerirut',views.gerirut),
    path('adm/deleteuser/<int:id>/',views.deleteuser),
    path('adm/deleteuserAP/<int:id>/',views.deleteuserAP),
    path('adm/aprovaruser/<int:id>/',views.aprovaruser),
    path('adm/pedirproc',views.listxml),
    path('adm/pedirproclist',views.listpedirproc),

    path('par/',views.par),
    path('par/addPrdtParc/',views.addPrdtParc),
    path('par/gerirParc/',views.gerirParc),
    path('par/gerirParc/deleteprdParc/<int:id>/',views.deleteprdParc),
    path('par/editarprod/<int:id>/',views.editarproc),

    path('cliente/', views.client),
    path('cliente/filtros', views.categorias),
    path('cliente/xbox', views.xbox_list),
    path('cliente/pc', views.pc_list),
    path('cliente/nintendo', views.nintendo_list),
    path('cliente/playstation', views.playstation_list),
    path('cliente/perfil', views.perfil),
    path('cliente/addcart/<int:id>/',views.addCartUser),
    path('cliente/cart', views.cart),
    path('cliente/finalizar/', views.finalizar),
    path('cliente/clientpage', views.orders_list),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
