########################
cmsplugin-photologue-pro
########################

This is another photologue plugin for Django CMS.


Requirements
============

  * Django
  * django-photologue
  * django-cms


Installation
============

Using PyPI you can simply type into a terminal:

    pip install cmsplugin-photologue-pro

or

    easy_install cmsplugin-photologue-pro


Configuration
=============

Add ``photologue`` and ``cmsplugin_photologue_pro`` to the list of
``INSTALLED_APPS`` in your ``settings.py`` file.
``python manage.py migrate cmsplugin_photologue_pro`` to update your database.
Add ``url(r'^cmsphotologue/', include('cmsplugin_photologue_pro.urls', namespace='cmsphotologue'))``
to your ``urls.py``.

Add custom gallery templates by adding something like the following to your settings.py:
```
PHOTOLOGUE_PRO_TEMPLATES = (
    ('cmsplugin_photologue_pro/gallery_plugin.html', _('Default')),
    ('custom_gallery.html', 'Custom Template'),
)
```

Author
======

Copyright 2012 Raphael Jasjukaitis <webmaster@raphaa.de>

Released under the BSD license.
