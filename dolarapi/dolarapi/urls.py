"""
URL configuration for dolarapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CriptoDolar.views import CargarTasasCriptoDolarCambioAPIView, TasaCambioCriptoDolarAPIView
from BCV.views import CargarTasasCambioAPIViewBCV, TasaCambioAPIViewBCV
from ExchangeMonitor.views import CargarTasasCambioAPIViewExMon, TasaCambioAPIViewExMon
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Para obtener tokens de acceso y refresco
    TokenRefreshView,  # Para refrescar el token de acceso
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Cripto-Dolar/', TasaCambioCriptoDolarAPIView.as_view(), name='Crypto-Dolar-api'),
    path('api/cargar-Cripto-Dolar/', CargarTasasCriptoDolarCambioAPIView.as_view(), name='cargar-CryptoDolar-api'),
    path('api/BCV/', TasaCambioAPIViewBCV.as_view(), name='BCV-api'),
    path('api/cargar-BCV', CargarTasasCambioAPIViewBCV.as_view(), name='cargar-BCV'),
    path('api/Exchange-Monitor/', TasaCambioAPIViewExMon.as_view(), name='ExchangeMonitor-api'),
    path('api/cargar-ExchangeMonitor', CargarTasasCambioAPIViewExMon.as_view(), name='cargar-ExchangeMonitor'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para obtener tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint para refrescar tokens
]

