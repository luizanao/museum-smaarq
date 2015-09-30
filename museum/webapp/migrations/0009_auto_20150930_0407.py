# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_thumbs.db.models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_image_img_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img_thumb',
        ),
        migrations.AlterField(
            model_name='image',
            name='img_image',
            field=django_thumbs.db.models.ImageWithThumbsField(upload_to=webapp.models.get_upload_path),
        ),
    ]
