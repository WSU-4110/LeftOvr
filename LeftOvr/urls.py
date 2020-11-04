"""LeftOvr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from htmlcss import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cont', views.cont, name='cont'),
    path('custHome', views.custHome, name='custHome'),
    path('custReg', views.custReg, name='custReg'),
    path('custSamp', views.custSamp, name='custSamp'),
    path('restHome', views.restHome, name='restHome'),
    path('restInp', views.restInp, name='restInp'),
    path('restReg', views.restReg, name='restReg'),
    path('sendMes', views.sendMes, name='sendMes'),
    path('wh', views.wh, name='why'),
    path('logI', views.logI, name='login'),
    path('action/', views.actionC, name='actionC'),
    path('act/', views.actionR, name='actionR'),
    path('acti/', views.actionCH, name='actionCH'),
    path('actio/', views.actionL, name='actionL'),
    path('new/', views.actionRH, name='actionRH'),
    path('restSamp', views.restSamp, name='restSamp'),
    path('new1/', views.actionRI, name='actionRI'),



   path('password-reset/',
         auth_views.PasswordResetView.as_view
         (template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view
         (template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view
         (template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
]
