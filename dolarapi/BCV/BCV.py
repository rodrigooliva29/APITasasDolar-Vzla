from .models import TasasCambioBCV
from pyDolarVenezuela.pages import BCV
from pyDolarVenezuela import Monitor
from datetime import datetime

def cargar_tasas_cambio():
    monitor = Monitor(BCV, 'USD')
    datos = monitor.get_value_monitors()

    datos_guardados = False

    for key, value in datos.items():
        print(f"Clave: {key}")
        if isinstance(value, dict):
            print("Valor:")
            for subkey, subvalue in value.items():
                print(f"  {subkey}: {subvalue}")
            print()  # Salto de línea entre cada par clave-valor
        else:
            print("Valor:", value)

        # Guardar datos en la base de datos
        if key != 'last_update':
            guardar_datos_local(key, value['title'], value['price'], value['price_old'], datos['last_update'])
            datos_guardados = True

    return datos_guardados

def guardar_datos_local(moneda, titulo, precio, precio_anterior, fecha_actualizacion_str):
    
    fecha_actualizacion = datetime.strptime(fecha_actualizacion_str, '%Y/%m/%d').date()

    if not TasasCambioBCV.objects.filter(fecha_actualizacion=fecha_actualizacion, moneda=moneda).exists():
        tasa = TasasCambioBCV(
            fecha_actualizacion=fecha_actualizacion,
            titulo=titulo,
            precio=precio,
            precio_anterior=precio_anterior,
            moneda=moneda,
        )
        tasa.save()
