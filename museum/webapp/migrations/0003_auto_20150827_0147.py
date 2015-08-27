# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20150827_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'Acervo', 'verbose_name_plural': 'Acervos'},
        ),
        migrations.AddField(
            model_name='collection',
            name='col_qr_code',
            field=models.ImageField(upload_to=b'', null=True, editable=False, blank=True),
        ),
    ]
