from .models import TasasCambioExMon
from pyDolarVenezuela.pages import ExchangeMonitor
from pyDolarVenezuela import Monitor
from datetime import datetime, time

def cargar_tasas_cambio():
    monitor = Monitor(ExchangeMonitor, 'USD')
    datos = monitor.get_value_monitors()
    datos_guardados = False

    for key, value in datos.items():
        # Convertir la fecha y hora al formato correcto
        fecha_hora_str = value['last_update']

        try:
            # Intentar convertir considerando fecha y hora
            fecha_hora = datetime.strptime(fecha_hora_str, '%d/%m/%Y, %I:%M %p')
        except ValueError:
            # Si falla, intentar solo como fecha y ajustar la hora a medianoche
            fecha_hora = datetime.strptime(fecha_hora_str, '%d/%m/%Y')
            fecha_hora = datetime.combine(fecha_hora.date(), time(0, 0))

        # Verificar si ya existe un registro con el mismo título y fecha
        if not TasasCambioExMon.objects.filter(titulo=value['title'], ultima_actualizacion=fecha_hora).exists():
            # Solo guardar si no existe ya un registro con el mismo título y fecha
            tasa = TasasCambioExMon(
                titulo=value['title'],
                precio=value['price'],
                ultima_actualizacion=fecha_hora
            )
            tasa.save()
            datos_guardados = True
        else:
            # Si ya existe, no guardar y quizás agregar un mensaje de depuración
            print(f"Registro con título '{value['title']}' y fecha '{fecha_hora}' ya existe.")

    return datos_guardados




