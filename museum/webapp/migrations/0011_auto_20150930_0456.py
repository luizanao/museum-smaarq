# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20150930_0428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='position',
            new_name='col_position',
        ),
        migrations.AlterField(
            model_name='image',
            name='img_image',
            field=models.ImageField(upload_to=webapp.models.get_upload_path, verbose_name=b'Imagem'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_thumb',
            field=models.ImageField(null=True, upload_to=webapp.models.get_upload_path, blank=True),
        ),
    ]
