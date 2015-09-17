# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from photologue import models as cms_models

PHOTOS_PER_PAGE = (
    (0, _('All')),
    (10, 10),
    (25, 25),
    (50, 50),
    (100, 100),
    (250, 250),
)


class Album(CMSPlugin):
    """Model for Album CMS plugin."""

    album = models.ForeignKey('photologue.Gallery', verbose_name=_('Album'))
    per_page = models.IntegerField(_('Photos per page'), choices=PHOTOS_PER_PAGE, default=100)
    photos_to_show = models.IntegerField(_('Photos_to_show'), default=getattr(cms_models, 'SAMPLE_SIZE', 6))
