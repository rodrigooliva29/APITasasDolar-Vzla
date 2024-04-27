from django.db import models

# Create your models here.

class TasasCambioBCV(models.Model):
    fecha_actualizacion = models.DateField()  # Fecha de actualización de la tasa de cambio
    moneda = models.CharField(max_length=3)  # Moneda (EUR, CNY, TRY, RUB, USD)
    titulo = models.CharField(max_length=100)  # Título de la moneda (ejemplo: Euro, Yuan chino)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de la moneda
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2)  # Precio anterior de la moneda
    
    class Meta:
        # Nombre singular que se mostrará en el panel de administración
        #verbose_name = "Tasa de Cambio BCV"
        # Nombre plural que se mostrará en el panel de administración
        verbose_name_plural = "Tasas de Cambio BCV"
    def __str__(self):
        # Por ejemplo, usando el título y la fecha de actualización
        return f"{self.id} - {self.titulo} - {self.fecha_actualizacion}"