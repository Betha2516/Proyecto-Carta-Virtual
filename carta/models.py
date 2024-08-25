from django.db import models

# Create your models here.
class Entrada(models.Model):
    name= models.CharField(max_length=200, default ="")
    descripcion = models.CharField(max_length=400, default="")
    img = models.URLField()

class PlatoF(models.Model):
    name= models.CharField(max_length=200, default ="")
    descripcion = models.CharField(max_length=400, default="")
    img = models.URLField()

class Bebida(models.Model):
    name= models.CharField(max_length=200, default ="")
    descripcion = models.CharField(max_length=400, default="")
    img = models.URLField()
    
class Postre(models.Model):
    name= models.CharField(max_length=200, default ="")
    descripcion = models.CharField(max_length=400, default="")
    img = models.URLField()
    
class Ubicaciones(models.Model):
    name= models.CharField(max_length=200, default ="")
    descripcion = models.CharField(max_length=400, default="")
    img = models.URLField()