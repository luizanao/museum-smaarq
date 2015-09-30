# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20150827_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='col_uuid',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='col_archeological_site',
            field=models.CharField(max_length=200, verbose_name='Sitio Arqueol\xf3gico'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='col_qr_code',
            field=models.ImageField(help_text=b'Este item \xc3\xa9 utilizado pelo app Android para identifica\xc3\xa7\xc3\xa3o das pe\xc3\xa7as.', upload_to=b'uploads/qr_codes/', null=True, verbose_name='QR Code de acesso ', blank=True),
        ),
    ]
