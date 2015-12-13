# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cantones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idCant', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
                ('idProvincia', models.IntegerField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='centros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idCentro', models.IntegerField(max_length=5)),
                ('clase', models.IntegerField(max_length=5)),
                ('tipo', models.IntegerField(max_length=5)),
                ('entidad', models.IntegerField(max_length=5)),
                ('sector', models.IntegerField(max_length=5)),
                ('farmacia', models.IntegerField(max_length=5)),
                ('idParroquia', models.IntegerField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='clases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idClas', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='entidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idEnt', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='farmacias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idFarm', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='parroquias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idParr', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
                ('idCanton', models.IntegerField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='provincias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idProv', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sectores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idSec', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tipos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idTip', models.IntegerField(max_length=5)),
                ('nombre', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
