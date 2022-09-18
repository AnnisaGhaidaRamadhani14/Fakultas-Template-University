"""untirta URL Configuration

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
from feb.views import prodi1
from feb.views import akreditas1
from fh.views import prodi2
from fh.views import akreditas2
from fisip.views import prodi3
from fisip.views import akreditas3
from fk.views import prodi4
from fk.views import akreditas4
from fkip.views import prodi5
from fkip.views import akreditas5
from ft.views import prodi6
from ft.views import akreditas6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feb/', prodi1),
    path('akreditasfeb/', akreditas1),
    path('fh/', prodi2),
    path('akreditasfh/', akreditas2),
    path('fisip/', prodi3),
    path('akreditasfisip/', akreditas3),
    path('fk/', prodi4),
    path('akreditasfk/', akreditas4),
    path('fkip/', prodi5),
    path('akreditasfkip/', akreditas5),
    path('ft/', prodi6),
    path('akreditasft/', akreditas6),
]
