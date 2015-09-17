# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_photologue_pro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='template',
            field=models.CharField(default=b'cmsplugin_photologue_pro/album_plugin.html', max_length=250, verbose_name='Template', choices=[('Default', b'cmsplugin_photologue_pro/album_plugin.html')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='photos_to_show',
            field=models.IntegerField(default=5, verbose_name='Photos to show'),
        ),
    ]
