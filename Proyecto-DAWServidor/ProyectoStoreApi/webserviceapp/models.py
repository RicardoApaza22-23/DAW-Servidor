# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    gmail = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=400)
    edad = models.IntegerField(blank=True, null=True)
    rol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
