from .models import TasaCambioCriptoDolar
from .serializers import TasaCambioCriptDolarSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from rest_framework import pagination
from .Cripto_Dolar import cargar_tasas_cambio


class TasaCambioCriptoDolarAPIView(APIView):
    pagination_class = pagination.PageNumberPagination  # Clase de paginación

    def get(self, request):
        # Crear un QuerySet base con todos los registros
        tasas = TasaCambioCriptoDolar.objects.all()

        # Obtener parámetros de filtrado de la solicitud
        id = request.query_params.get('id', None)
        titulo = request.query_params.get('titulo', None)
        ultima_actualizacion = request.query_params.get('ultima_actualizacion', None)

        # Aplicar filtros condicionalmente según los parámetros proporcionados
        if id is not None:
            tasas = tasas.filter(id=id)  # Filtrar por ID

        if titulo:
            tasas = tasas.filter(titulo=titulo)  # Filtrar por título

        if ultima_actualizacion:
            try:
                fecha = datetime.strptime(ultima_actualizacion, '%Y-%m-%d').date()
                tasas = tasas.filter(ultima_actualizacion=fecha)  # Filtrar por fecha
            except ValueError:
                return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD.'}, status=400)

        # Aplicar la paginación después del filtrado
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(tasas, request)  # Paginar el QuerySet filtrado

        # Si hay una página válida, devolver la respuesta paginada
        if page:
            serializer = TasaCambioCriptDolarSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        # Si no hay página (caso raro), devolver el `QuerySet` completo
        serializer = TasaCambioCriptDolarSerializer(tasas, many=True)
        return Response(serializer.data)


class CargarTasasCriptoDolarCambioAPIView(APIView):
    def post(self, request, format=None):
        datos_guardados = cargar_tasas_cambio()  # Llama a la función para cargar los datos
        if datos_guardados:
            return Response({'message': 'Tasas de cambio cargadas correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'No se han encontrado nuevas tasas de cambio para cargar'}, status=status.HTTP_200_OK)