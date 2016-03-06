# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import overview, gallery, photo


urlpatterns = [
    url(r'^$', overview, name='photologue_overview'),
    url(r'^(?P<album>\d+)/$', gallery, name='photologue_album'),
    url(r'^(?P<album>\d+)/(?P<photo>\d+)/$', photo, name='photologue_photo'),
]
