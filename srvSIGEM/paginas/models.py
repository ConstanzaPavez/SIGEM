from django.db import models

class Articulo(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
    tipo_dano = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='inventario/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tipo_dano = models.TextField()
    responsable = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.responsable}"