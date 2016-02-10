# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCentrosMedicos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cantones',
        ),
        migrations.CreateModel(
            name='Cantones',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'cantones',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Centros',
        ),
        migrations.CreateModel(
            name='Centros',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'managed': True,
                'db_table': 'centros',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Clases',
        ),
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField(blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'clases',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centros',
            name='idclase',
            field=models.ForeignKey(null=True, db_column='idclase', blank=True, to='appCentrosMedicos.Clases'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Entidades',
        ),
        migrations.CreateModel(
            name='Entidades',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'entidades',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centros',
            name='identidad',
            field=models.ForeignKey(null=True, db_column='identidad', blank=True, to='appCentrosMedicos.Entidades'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Farmacias',
        ),
        migrations.CreateModel(
            name='Farmacias',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'farmacias',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centros',
            name='idfarmacia',
            field=models.ForeignKey(null=True, db_column='idfarmacia', blank=True, to='appCentrosMedicos.Farmacias'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Parroquias',
        ),
        migrations.CreateModel(
            name='Parroquias',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
                ('idcanton', models.ForeignKey(null=True, db_column='idcanton', blank=True, to='appCentrosMedicos.Cantones')),
            ],
            options={
                'managed': True,
                'db_table': 'parroquias',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centros',
            name='idparroquia',
            field=models.ForeignKey(null=True, db_column='idparroquia', blank=True, to='appCentrosMedicos.Parroquias'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Provincias',
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'provincias',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cantones',
            name='idprovincia',
            field=models.ForeignKey(null=True, db_column='idprovincia', blank=True, to='appCentrosMedicos.Provincias'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Sectores',
        ),
        migrations.CreateModel(
            name='Sectores',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'sectores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centros',
            name='idsector',
            field=models.ForeignKey(null=True, db_column='idsector', blank=True, to='appCentrosMedicos.Sectores'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Tipos',
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'tipos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centros',
            name='idtipo',
            field=models.ForeignKey(null=True, db_column='idtipo', blank=True, to='appCentrosMedicos.Tipos'),
            preserve_default=True,
        ),
    ]
