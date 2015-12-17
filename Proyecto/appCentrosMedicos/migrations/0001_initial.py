# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cantones',
            fields=[
            ],
            options={
                'db_table': 'cantones',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Centros',
            fields=[
            ],
            options={
                'db_table': 'centros',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clases',
            fields=[
            ],
            options={
                'db_table': 'clases',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entidades',
            fields=[
            ],
            options={
                'db_table': 'entidades',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Farmacias',
            fields=[
            ],
            options={
                'db_table': 'farmacias',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parroquias',
            fields=[
            ],
            options={
                'db_table': 'parroquias',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sectores',
            fields=[
            ],
            options={
                'db_table': 'sectores',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
            ],
            options={
                'db_table': 'tipos',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
