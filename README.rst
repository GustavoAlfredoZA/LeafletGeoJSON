=============
Mezzanine-map
=============

Plugin for mezzanine

Quick start
------------

1.- Add mezzanine map to INSTALLED_APPS
INSTALLED_APPS = [
        ...
        'mezzanine_map',
    ]
2.- Include the polls URLconf in your project urls.py like this::

    path('map/', include('mezzanine_map.urls')),
