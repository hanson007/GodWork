from django.conf.urls import include, url
from Service.views  import *

urlpatterns = [
    url(r'list/', list),
    url(r'content/(?P<ids>\d{1,3})', content),
    url(r"getCpu",getCpu),
    url(r"push_data/", push_data)
]