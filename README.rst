=============
Mezzanine-map
=============

Plugin for mezzanine

Quick start
------------

1.-Install leaflet for django::

    pip install django-leaflet

2.- Add mezzanine map to INSTALLED_APPS
  INSTALLED_APPS = [
    ...
    'mezzanine_gasStation_map',
  ]
3.- Include the polls URLconf in your project urls.py like this::

    path('map/', include('mezzanine_gasStation_map.urls')),
