from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import pagination
from .models import TasasCambioBCV
from .serializers import TasaCambioSerializerBCV
from .BCV import cargar_tasas_cambio
from datetime import datetime
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TasaCambioAPIViewBCV(APIView):

    pagination_class = pagination.PageNumberPagination

    def get(self, request):
        # Obtener el QuerySet base
        tasas = TasasCambioBCV.objects.all()  # Todos los registros

        # Obtener parámetros de filtrado
        id = request.query_params.get('id', None)
        titulo = request.query_params.get('titulo', None)
        fecha_actualizacion = request.query_params.get('fecha_actualizacion', None)

        # Aplicar filtros según los parámetros proporcionados
        if id is not None:
            tasas = tasas.filter(id=id)  # Filtrar por ID

        if titulo is not None:
            tasas = tasas.filter(titulo=titulo)  # Filtrar por título

        if fecha_actualizacion is not None:
            # Convertir la fecha a objeto datetime.date
            try:
                fecha = datetime.strptime(fecha_actualizacion, '%Y-%m-%d').date()
                tasas = tasas.filter(fecha_actualizacion=fecha)  # Filtrar por fecha
            except ValueError:
                return Response({'error': 'Formato de fecha inválido, use YYYY-MM-DD'}, status=400)

        # Paginar el QuerySet después de filtrar
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(tasas, request)  # Paginar el QuerySet filtrado

        # Si hay una página, devolver la respuesta paginada
        if page is not None:
            serializer = TasaCambioSerializerBCV(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        # Si no hay página, devolver todo el QuerySet
        serializer = TasaCambioSerializerBCV(tasas, many=True)
        return Response(serializer.data)


class CargarTasasCambioAPIViewBCV(APIView):
    authentication_classes = [JWTAuthentication]  # Requerir JWTAuthentication
    permission_classes = [IsAuthenticated]  # Requerir autenticación

    def post(self, request, format=None):

        datos_guardados = cargar_tasas_cambio()  # Llama a la función para cargar los datos
        if datos_guardados:
            return Response({'message': 'Tasas de cambio cargadas correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'No se han encontrado nuevas tasas de cambio para cargar'}, status=status.HTTP_200_OK)
