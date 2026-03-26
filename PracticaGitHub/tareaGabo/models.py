from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
