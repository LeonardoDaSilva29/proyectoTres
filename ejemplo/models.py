from django.db import models


class Familiar(models.Model):
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    #creado_el = models.DateTimeField() 
    #actualizado_el = models.DateTimeField()

    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Mascotas(models.Model):
    
    nombre = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    edad = models.IntegerField()
    

    def __str__(self):
      return f"{self.nombre}, {self.color}, {self.edad} años"

class Vehiculos(models.Model):
    
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año = models.IntegerField()

    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.año}"