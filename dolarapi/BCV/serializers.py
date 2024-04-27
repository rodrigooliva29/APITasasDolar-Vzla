from rest_framework import serializers
from .models import TasasCambioBCV

class TasaCambioSerializerBCV(serializers.ModelSerializer):
    class Meta:
        model = TasasCambioBCV
        fields = 'fecha_actualizacion', 'moneda', 'titulo', 'precio', 'precio_anterior'