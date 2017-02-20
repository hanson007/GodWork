from django.conf.urls import include, url
from Api.views import *

urlpatterns = [
    url(r"savedata",savedata),
    url(r"setcpu",setcpu),
    url(r"doCommand",doCommand),
    url(r"test", test),
]