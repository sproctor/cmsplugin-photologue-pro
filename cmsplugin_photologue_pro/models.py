# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.models import CMSPlugin
from photologue import models as photologue_models

PHOTOS_PER_PAGE = (
    (0, _('All')),
    (10, 10),
    (25, 25),
    (50, 50),
    (100, 100),
    (250, 250),
)

PHOTOLOGUE_PRO_TEMPLATES_DEFAULT_TEMPLATE = 'cmsplugin_photologue_pro/album_plugin.html'
PHOTOLOGUE_PRO_TEMPLATES_CHOICES = getattr(settings, 'PHOTOLOGUE_PRO_TEMPLATES',
                                           (
                                               (PHOTOLOGUE_PRO_TEMPLATES_DEFAULT_TEMPLATE, _('Default')),
                                           ))


class Album(CMSPlugin):
    """Model for Album CMS plugin."""

    album = models.ForeignKey(photologue_models.Gallery, verbose_name=_('Album'))
    per_page = models.IntegerField(_('Photos per page'), choices=PHOTOS_PER_PAGE, default=100)
    photos_to_show = models.IntegerField(_('Photos to show'), default=getattr(photologue_models, 'SAMPLE_SIZE', 6))
    template = models.CharField(_('Template'), max_length=250, choices=PHOTOLOGUE_PRO_TEMPLATES_CHOICES,
                                default=PHOTOLOGUE_PRO_TEMPLATES_DEFAULT_TEMPLATE)
    show_photo_title = models.BooleanField(_('Show photo title'), default=True)
