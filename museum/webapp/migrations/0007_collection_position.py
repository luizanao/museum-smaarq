# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20150930_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='position',
            field=geoposition.fields.GeopositionField(default='', max_length=42),
            preserve_default=False,
        ),
    ]
