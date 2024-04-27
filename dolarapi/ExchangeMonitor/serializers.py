from rest_framework import serializers
from .models import TasasCambioExMon

class TasaCambioSerializerExMon(serializers.ModelSerializer):
    class Meta:
        model = TasasCambioExMon
        fields = 'titulo', 'precio', 'ultima_actualizacion'