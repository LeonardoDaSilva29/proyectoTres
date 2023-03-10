"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (AltaMascotas, index, mostrar_vehiculos, saludar_a, sumar, buscar, mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, 
                            mostrar_mascotas, BuscarMascota, ActualizarMascotas, BorrarMascotas, BuscarVehiculo, AltaVehiculos, ActualizarVehiculos, BorrarVehiculo)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCION !!!
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/', buscar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()),
    # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA actualizar FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()), # NUEVA RUTA PARA borrar FAMILIAR

    path('mi-mascota/', mostrar_mascotas),
    path('mi-mascota/buscar', BuscarMascota.as_view()),
    path('mi-mascota/alta', AltaMascotas.as_view()),
    path('mi-mascota/actualizar/<int:pk>', ActualizarMascotas.as_view()), 
    path('mi-mascota/borrar/<int:pk>', BorrarMascotas.as_view()),

    path('mi-vehiculo/', mostrar_vehiculos),
    path('mi-vehiculo/buscar', BuscarVehiculo.as_view()),
    path('mi-vehiculo/alta', AltaVehiculos.as_view()),
    path('mi-vehiculo/actualizar/<int:pk>', ActualizarVehiculos.as_view()),
    path('mi-vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),

]