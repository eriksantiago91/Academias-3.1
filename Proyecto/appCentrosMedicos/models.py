from django.db import models

# Create your models here.
class centros(models.Model):
    idCentro  = models.IntegerField(max_length=5)
    clase = models.IntegerField(max_length=5)
    tipo = models.IntegerField(max_length=5)
    entidad = models.IntegerField(max_length=5)
    sector = models.IntegerField(max_length=5)
    farmacia = models.IntegerField(max_length=5)
    idParroquia = models.IntegerField(max_length=5)

class provincias(models.Model):
    idProv  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)

class cantones(models.Model):
    idCant  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)
    idProvincia  = models.IntegerField(max_length=5)

class parroquias(models.Model):
    idParr  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)
    idCanton  = models.IntegerField(max_length=5)

class clases(models.Model):
    idClas  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)

class sectores(models.Model):
    idSec  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)

class tipos(models.Model):
    idTip  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)

class farmacias(models.Model):
    idFarm  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)

class entidades(models.Model):
    idEnt  = models.IntegerField(max_length=5)
    nombre = models.TextField(max_length=200)
