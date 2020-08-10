"""onlinetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from users.views import indexView
from django.contrib import admin
from django.urls import path
from users import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('',indexView,name="index"),
    url(r'^home/$', views.home, name="home"),
    url(r'^about/$', views.about, name='about'),
    url(r'^bloghome/$', views.bloghome, name='bloghome'),
    url(r'^blogsingle/$', views.blogsingle, name='blogsingle'),
    url(r'^elements/$', views.elements, name='elements'),
    url(r'^hotels/$', views.hotels , name='hotels'),
    url(r'^insurance/$', views.insurance, name='insurance'),
    url(r'^packages/$', views.packages, name='packages'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^Home/$', views.Home , name='Home'),
    url(r'^Practice/$', views.Practice, name='Practice'),
    url(r'^Events/$', views.Events, name='Events'),
    url(r'^Test/$', views.Test, name='Test'),
    
    
]


