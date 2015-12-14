# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Cantones(models.Model):
    idcanton = models.IntegerField(db_column='idCanton', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    idprovincia = models.IntegerField(db_column='idProvincia', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)  # AutoField?
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'cantones'


class Centros(models.Model):
    idcentro = models.IntegerField(db_column='idCentro', blank=True, null=True)  # Field name made lowercase.
    idclase = models.IntegerField(db_column='idClase', blank=True, null=True)  # Field name made lowercase.
    idtipo = models.IntegerField(db_column='idTipo', blank=True, null=True)  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad', blank=True, null=True)  # Field name made lowercase.
    idsector = models.IntegerField(db_column='idSector', blank=True, null=True)  # Field name made lowercase.
    idfarmacia = models.IntegerField(db_column='idFarmacia', blank=True, null=True)  # Field name made lowercase.
    idparroquia = models.IntegerField(db_column='idParroquia', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.idtipo
    class Meta:
        managed = False
        db_table = 'centros'


class Clases(models.Model):
    idclase = models.IntegerField(db_column='idClase', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'clases'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entidades(models.Model):
    identidad = models.IntegerField(db_column='idEntidad', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'entidades'


class Farmacias(models.Model):
    idfarmacia = models.IntegerField(db_column='idFarmacia', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'farmacias'


class Parroquias(models.Model):
    idparroquia = models.IntegerField(db_column='idParroquia', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    idcanton = models.IntegerField(db_column='idCanton', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'parroquias'


class Provincias(models.Model):
    idprovincia = models.IntegerField(db_column='idProvincia', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'provincias'


class Sectores(models.Model):
    idsector = models.IntegerField(db_column='idSector', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'sectores'


class Tipos(models.Model):
    idtipo = models.IntegerField(db_column='idTipo', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'tipos'
