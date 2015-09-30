# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20150930_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_thumb',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'Imagem'),
        ),
    ]
