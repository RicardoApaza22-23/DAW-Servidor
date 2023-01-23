# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comentario(models.Model):
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    comentario = models.CharField(max_length=1000, blank=True, null=True)
    valoracion = models.IntegerField(blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'comentario'


class Comprado(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_comprador = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_comprador')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'comprado'


class Favoritos(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'favoritos'


class Producto(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    vendedor = models.CharField(max_length=250, blank=True, null=True)
    estacion = models.CharField(max_length=150, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=250, blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    categoria = models.CharField(max_length=250, blank=True, null=True)
    fecha_de_subida = models.DateField()

    class Meta:
        managed = False
        db_table = 'producto'


class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=400)
    edad = models.IntegerField(blank=True, null=True)
    rol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
