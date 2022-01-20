from distutils.command import upload
from email import charset
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Ciudad(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ciudades'
        verbose_name_plural = 'ciudades'

class Usuario(models.Model):

    genero_eleccion = (
        ('M' , 'Masculino'),
        ('F' , 'Femenino')
    )
    codigo = models.IntegerField()
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    genero = models.CharField(choices=genero_eleccion , max_length=100)
    ciudad = models.ForeignKey(Ciudad , on_delete=models.PROTECT)

    def __str__(self):
        return (self.nombre)