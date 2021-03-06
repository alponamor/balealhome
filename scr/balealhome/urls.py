"""balealhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from balealhome.cashflow import views

urlpatterns = [
    url(r'^$', views.hi_page, name = 'hi_page'),                 # это стартовая страница для неавторизованных юзеров
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', views.account_profile, name = 'account_profile'), # стартовая страница администратора, пока по номеру(?), по именю м.б. потом
    url(r'^i18n/', include('django.conf.urls.i18n')), # для смены языка - НЕ РАБОТАЕТ!
]
