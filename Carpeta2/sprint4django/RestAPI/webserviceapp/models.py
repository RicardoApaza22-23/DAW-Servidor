# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tcomentarios(models.Model):
    comentarios = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING, blank=True, null=True)
    juegos = models.ForeignKey('Tjuegos', models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tComentarios'


class Tfavoritos(models.Model):
    idusuario = models.ForeignKey('Tusuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idjuego = models.ForeignKey('Tjuegos', models.DO_NOTHING, db_column='idJuego')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tFavoritos'


class Tjuegos(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    url_image = models.CharField(max_length=200, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    pegi = models.CharField(db_column='PEGI', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tJuegos'


class Tusuarios(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200, blank=True, null=True)
    contraseña = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tUsuarios'
