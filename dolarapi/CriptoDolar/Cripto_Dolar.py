
from pyDolarVenezuela.pages import CriptoDolar
from pyDolarVenezuela import Monitor
from datetime import datetime, date
from .models import TasaCambioCriptoDolar

def cargar_tasas_cambio():
    monitor = Monitor(CriptoDolar, 'USD')
    datos = monitor.get_value_monitors()
    datos_guardados = False

    for key, value in datos.items():
        # Convertir la fecha y hora al formato correcto
        fecha_hora_str = value['last_update']
        fecha_hora = datetime.strptime(fecha_hora_str, '%d/%m/%Y, %I:%M %p')

        # Filtrar utilizando un rango para la fecha
        fecha_inicio = datetime.combine(fecha_hora.date(), datetime.min.time())
        fecha_fin = datetime.combine(fecha_hora.date(), datetime.max.time())

        # Verificar si ya existe un registro en el mismo día con el mismo título
        if not TasaCambioCriptoDolar.objects.filter(
                ultima_actualizacion__gte=fecha_inicio,
                ultima_actualizacion__lte=fecha_fin,
                titulo=value['title']
        ).exists():
            # Guardar el nuevo resultado
            tasa = TasaCambioCriptoDolar(
                titulo=value['title'],
                precio=value['price'],
                tipo=value['type'],
                ultima_actualizacion=fecha_hora  # Se guarda como datetime completo
            )
            tasa.save()
            datos_guardados = True

    return datos_guardados