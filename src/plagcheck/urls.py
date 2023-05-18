"""plagcheck URL Configuration

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
from paras.views import home_view, result_view, role_v, login_f, login_u, add, fmenu_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check', home_view, name='home'),
    path('results', result_view, name='result'),
    path('', role_v, name="role"),
    path('login/', login_f, name="logf"),
    path('loginu/', login_u, name="logu"),
    path('addnew/', add, name="new"),
    path('facmain/', fmenu_v, name="fac" )



]
