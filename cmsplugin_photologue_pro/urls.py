# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import overview, gallery, photo

urlpatterns = [
    url(r'^$', overview, name='overview'),
    url(r'^(?P<album>\d+)/$', gallery, name='album'),
    url(r'^(?P<album>\d+)/(?P<photo>\d+)/$', photo, name='photo'),
]
