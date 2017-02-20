"""GodWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from views import *
from GodWork.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^$', index),
    url(r'^base/', base),
    url(r'^login/', login),
    url(r"^register/",register),

    url(r'^test/',test),
    url(r'^logout/', logout),

    url(r'^404/(?P<error>\w+)',forbiden),

    url(r'^service/',include('Service.urls')),
    url(r'^api/', include('Api.urls')),
    url(r'^user/', include('User.urls')),

]
