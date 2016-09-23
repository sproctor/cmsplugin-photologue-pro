# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.utils.translation import ugettext_lazy as _

from cms.models.pagemodel import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_photologue_pro import models as pluginmodels
from photologue import models


class GalleryPlugin(CMSPluginBase):
    """Gallery CMS plugin."""

    name = _('Gallery')
    model = pluginmodels.Gallery
    _render_template = 'cmsplugin_photologue_pro/gallery_plugin.html'

    def get_render_template(self, context, instance, placeholder):
        return self._render_template if not instance.template else instance.template

    def render(self, context, instance, placeholder):
        if not instance.album.is_public:
            context.update({'is_not_public': True})
            return context
        photo_instance = instance.album.photos.filter(is_public=True)
        photo_instance = photo_instance
        photos_number = instance.album.photos.count()
        per_page = instance.per_page or 10000
        photos_to_show = instance.photos_to_show
        paginator = Paginator(photo_instance, per_page)
        try:
            page = max(int(context.get('request', 1).GET.get('page', 1)))
        except (ValueError, TypeError):
            page = 1
        try:
            photos = paginator.page(page)
        except (EmptyPage, InvalidPage):
            photos = paginator.page(paginator.num_pages)
        context.update({
            'gallery': instance.album,
            'photos': photos,
            'pages': paginator.page_range,
            'current_page': page,
            'photos_to_show': photos_to_show,
            'photos_number': photos_number,
        })
        return context

plugin_pool.register_plugin(GalleryPlugin)
