from django.conf.urls import url, include#, patterns
#from django.conf.urls.defaults import *
#import views
from mezzanine_map.views import map_View,map

urlpatterns = [
    url(r'^map', map_View.as_view()),
]
