# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_photologue_pro', '0002_auto_20150917_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='show_photo_title',
            field=models.BooleanField(default=True, verbose_name='Show photo title'),
        ),
        migrations.AlterField(
            model_name='album',
            name='template',
            field=models.CharField(default=b'cmsplugin_photologue_pro/album_plugin.html', max_length=250, verbose_name='Template', choices=[(b'Default', b'cmsplugin_photologue_pro/album_plugin.html'), (b'Carousel V1', b'cmsplugin_photologue_pro/carousel_v1.html')]),
        ),
    ]
