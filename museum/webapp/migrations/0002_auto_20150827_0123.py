# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='col_discover_date',
            field=models.DateField(null=True, verbose_name='Data de Descoberta', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='col_origin_date',
            field=models.DateField(null=True, verbose_name='Data de Origem', blank=True),
        ),
    ]
