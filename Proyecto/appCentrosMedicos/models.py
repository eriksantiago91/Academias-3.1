# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Cantones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    idprovincia = models.ForeignKey('Provincias', db_column='idprovincia', blank=True, null=True)
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'cantones'


class Centros(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idclase = models.ForeignKey('Clases', db_column='idclase', blank=True, null=True)
    idtipo = models.ForeignKey('Tipos', db_column='idtipo', blank=True, null=True)
    identidad = models.ForeignKey('Entidades', db_column='identidad', blank=True, null=True)
    idsector = models.ForeignKey('Sectores', db_column='idsector', blank=True, null=True)
    idfarmacia = models.ForeignKey('Farmacias', db_column='idfarmacia', blank=True, null=True)
    idparroquia = models.ForeignKey('Parroquias', db_column='idparroquia', blank=True, null=True)
    def __str__ (self):
        return self.id
    class Meta:
        managed = True
        db_table = 'centros'


class Clases(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField(blank=True)
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'clases'


class Entidades(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'entidades'


class Farmacias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'farmacias'


class Parroquias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    idcanton = models.ForeignKey(Cantones, db_column='idcanton', blank=True, null=True)
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'parroquias'


class Provincias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'provincias'


class Sectores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'sectores'


class Tipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.TextField()
    def __str__ (self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'tipos'
