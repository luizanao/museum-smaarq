# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20150930_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='col_qr_code',
            field=models.ImageField(upload_to=b'uploads/qr_codes/', editable=False, blank=True, help_text=b'Este item \xc3\xa9 utilizado pelo app Android para identifica\xc3\xa7\xc3\xa3o das pe\xc3\xa7as.', null=True, verbose_name='QR Code de acesso '),
        ),
        migrations.AlterField(
            model_name='collection',
            name='col_uuid',
            field=models.CharField(max_length=200, editable=False),
        ),
    ]
