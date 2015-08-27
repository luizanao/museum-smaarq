# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20150827_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='col_qr_code',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
