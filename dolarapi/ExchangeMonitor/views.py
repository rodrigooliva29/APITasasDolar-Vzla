from .models import TasasCambioExMon
from .serializers import TasaCambioSerializerExMon
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import pagination
from datetime import datetime
from .ExMon import cargar_tasas_cambio

# Create your views here.


class TasaCambioAPIViewExMon(APIView):
    # Definir la clase de paginación
    pagination_class = pagination.PageNumberPagination
    
    def get(self, request):
        # Obtener el QuerySet base
        tasas = TasasCambioExMon.objects.all()

        # Obtener parámetros de la solicitud para filtrar
        id = request.query_params.get('id', None)
        titulo = request.query_params.get('titulo', None)
        ultima_actualizacion = request.query_params.get('ultima_actualizacion', None)

        # Aplicar filtros según los parámetros proporcionados
        if id is not None:
            tasas = tasas.filter(id=id)  # Filtrar por ID

        if titulo is not None:
            tasas = tasas.filter(titulo=titulo)  # Filtrar por título

        if ultima_actualizacion is not None:
            # Convertir a objeto datetime.date
            try:
                fecha = datetime.strptime(ultima_actualizacion, '%Y-%m-%d').date()
                tasas = tasas.filter(ultima_actualizacion=fecha)  # Filtrar por fecha
            except ValueError:
                return Response({'error': 'Formato de fecha inválido, use YYYY-MM-DD'}, status=400)

        # Aplicar la paginación
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(tasas, request)  # Paginar después del filtrado
        
        # Si hay página, devolver la respuesta paginada
        if page is not None:
            serializer = TasaCambioSerializerExMon(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        # Si no hay página (raro), devolver todo el QuerySet
        serializer = TasaCambioSerializerExMon(tasas, many=True)
        return Response(serializer.data)


class CargarTasasCambioAPIViewExMon(APIView):
    def post(self, request, format=None):
        datos_guardados = cargar_tasas_cambio()  # Llama a la función para cargar los datos
        if datos_guardados:
            return Response({'message': 'Tasas de cambio cargadas correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'No se han encontrado nuevas tasas de cambio para cargar'}, status=status.HTTP_200_OK)
        