from django.db import models

# Create your models here.

class TasaCambioCriptoDolar(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    ultima_actualizacion = models.DateField()

    class Meta:
        # Nombre singular que se mostrará en el panel de administración
        #verbose_name = "Tasa de Cambio BCV"
        # Nombre plural que se mostrará en el panel de administración
        verbose_name_plural = "Tasas de Cambio Cripto Dolar"
    def __str__(self):
        # Por ejemplo, usando el título y la fecha de actualización
        return f"{self.id} - {self.titulo} - {self.ultima_actualizacion}"