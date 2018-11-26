"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views


#This file basically will hold ythe url with app(page) name.
#As we have maked first music app(page) so when user will request to music in url pattern first request will come to
# this section but we want to give it to music app section so we have added url for music app bellow.
urlpatterns = [
  #url(r'^admin/', admin.site.urls),
  #path('', views.homepage),             #this is default url it will call homepage() function from views.py
  #path('contact', views.contact),        #this is second url it will call contact() function from views.py for that give url/contact
  #path('', views.template_homepage),     # this url will directly call template_homepage() function fron views.py and there render function will call home.html file from templates folder.
 path('home2/', views.template_homepage2, name="main_page"),  # this url will call template_homepage2() function and there once user clicks count button it will call following url automatically
  path('wordcount/',views.count,name="count"), # this url will be called once user clicked on count button from form. this url will be identified by its name not by its url in form.
  #url(r'^music/', include('music.urls')),
]
