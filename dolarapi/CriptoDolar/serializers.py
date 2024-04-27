from rest_framework import serializers
from .models import TasaCambioCriptoDolar


class TasaCambioCriptDolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasaCambioCriptoDolar
        fields = 'titulo', 'precio', 'ultima_actualizacion'
