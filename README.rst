=============
Mezzanine-map
=============

Plugin for mezzanine

Quick start
------------

1.-Install leaflet for django::

    pip install django-leaflet

2.- Add mezzanine map to INSTALLED_APPS::

  INSTALLED_APPS = [
    ...
    'leaflet',
    'mezzanine_gasStation_map',
    ...
  ]

3.- Include the polls URLconf in yourProject/yourProject/urls.py like this::

    path('map/', include('mezzanine_gasStation_map.urls')),

4.- Include in yourProject/yourProject/urls.py::

    import mezzanine_gasStation_map.urls

5.- Create links in yourProject::

    ln /home/user/git/LeafletGeoJSON/mezzanine_gasStation_map .
    ln /home/user/git/LeafletGeoJSON/mezzanine_gasStation_map/static ./static
    ln /home/user/git/LeafletGeoJSON/mezzanine_gasStation_map/templates ./templates
