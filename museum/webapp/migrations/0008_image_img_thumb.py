# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_collection_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_thumb',
            field=models.ImageField(default='', upload_to=webapp.models.get_upload_path, editable=False),
            preserve_default=False,
        ),
    ]
