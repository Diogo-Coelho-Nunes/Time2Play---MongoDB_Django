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
    path('c1/sales/', views.addSale),

    path('adm/',views.adm),
    path('adm/aprpar',views.aprpar),
    path('adm/criarut',views.criarut),
    path('adm/gerirut',views.gerirut),
    path('adm/deleteuser/<int:id>/',views.deleteuser),
    path('adm/deleteuserAP/<int:id>/',views.deleteuserAP),
    path('adm/aprovaruser/<int:id>/',views.aprovaruser),

    path('par/',views.par),
    path('par/addPrdtParc/',views.addPrdtParc),
    path('par/gerirParc/',views.gerirParc),
    path('par/gerirParc/deleteprdParc/<int:id>/',views.deleteprdParc),
    path('par/editarprod/<int:id>/',views.editarproc),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
