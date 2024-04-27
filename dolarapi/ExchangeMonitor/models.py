from django.db import models

# Create your models here.
class TasasCambioExMon(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ultima_actualizacion = models.DateField()
    percent = models.CharField(max_length=10)
    change = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)

    class Meta:
        # Nombre singular que se mostrará en el panel de administración
        #verbose_name = "Tasa de Cambio BCV"
        # Nombre plural que se mostrará en el panel de administración
        verbose_name_plural = "Tasas de Cambio Exchange Monitor"

    def __str__(self):
        # Por ejemplo, usando el título y la fecha de actualización
        return f"{self.id} - {self.titulo} - {self.ultima_actualizacion}"