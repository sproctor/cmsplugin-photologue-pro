# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0009_auto_20150907_2310'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('per_page', models.IntegerField(default=100, verbose_name='Photos per page', choices=[(0, 'All'), (10, 10), (25, 25), (50, 50), (100, 100), (250, 250)])),
                ('photos_to_show', models.IntegerField(default=5, verbose_name='Photos_to_show')),
                ('album', models.ForeignKey(verbose_name='Album', to='photologue.Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
