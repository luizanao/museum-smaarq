# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('col_itemname', models.CharField(max_length=200, verbose_name='Nome da Pe\xe7a')),
                ('col_archeological_site', models.CharField(max_length=200, verbose_name='Nome da Pe\xe7a')),
                ('col_description', redactor.fields.RedactorField(verbose_name='Descri\xe7\xe3o do Item')),
                ('col_origin_date', models.DateField(verbose_name='Data de Origem', blank=True)),
                ('col_discover_date', models.DateField(verbose_name='Data de Descoberta', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Acervos',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_image', models.ImageField(upload_to=webapp.models.get_upload_path, verbose_name=b'Imagem')),
                ('img_description', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o breve', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'Galeria de Imagens',
            },
        ),
    ]
