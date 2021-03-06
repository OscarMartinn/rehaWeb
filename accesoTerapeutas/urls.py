from django.urls import path
from . import views 

urlpatterns = [

    path('', views.acceso, name="Acceso"),
    path('setLanguage/<int:idLanguage>/<int:idSeccion>', views.setLanguage, name = "setLanguage"),

    # INFORMES
    path('informes', views.informes, name="Informes"),
    path('informes/<int:sesionId>', views.informes, name="Informes"),
    path('informes/<int:sesionId>/<str:showFilters>', views.informes, name="Informes"),
    path('generarPDF/<int:sesionId>', views.generarPDF, name="generarPDF"),
    path('informes/filtrarInforme/<int:idPaciente>/<int:sesionId>', views.filtrarInforme, name="filtrarInforme"),
 
    # PACIENTES
    path('pacientes', views.pacientes, name="Pacientes"),
    path('busquedaPacientes', views.busquedaPacientes, name="BusquedaPacientes"),
    path('infoPaciente/<int:idPaciente>', views.infoPaciente, name="InfoPaciente"),
    path('editarPaciente/<int:idPaciente>', views.editarPaciente, name="EditarPaciente"),
    path('nuevoPaciente', views.nuevoPaciente, name="NuevoPaciente"),
    path('ocultarPaciente/<int:idPaciente>', views.ocultarPaciente, name="Ocultar"),
    path('pacientesNoVisibles', views.pacientesNoVisibles, name="PacientesNoVisibles"),

    # EJERCICIOS
    path('ejercicios', views.ejercicios, name="Ejercicios"),
    path('busquedaEjercicios', views.busquedaEjercicios, name="BusquedaEjercicios"),
    path('nuevoEjercicio', views.nuevoEjercicio, name="NuevoEjercicio"),
    path('editarEjercicio/<int:idEjercicio>', views.editarEjercicio, name="EditarEjercicio"),
    path('ocultarEjercicio/<int:idEjercicio>', views.ocultarEjercicio, name="OcultarEjercicio"),
    path('infoEjercicio/<int:idEjercicio>', views.infoEjercicio, name="InfoEjercicio"),
    path('ejerciciosNoVisibles', views.ejerciciosNoVisibles, name="EjerciciosNoVisibles"),


    path('subirVideo/<int:idEjercicio>', views.subirVideo, name="subirVideo"),



    # SESIONES
    path('sesiones', views.sesiones, name="Sesiones"),
    path('busquedaSesiones', views.busquedaSesiones, name="BusquedaSesiones"),
    path('sesionesNoVisibles', views.sesionesNoVisibles, name="SesionesNoVisibles"),
    path('sesionEnviada/<int:sesionId>', views.sesionEnviada, name="SesionEnviada"),
    path('nuevaSesion', views.nuevaSesion, name="NuevaSesion"),
    path('ocultarSesion/<int:idSesion>', views.ocultarSesion, name="OcultarSesion"),
    path('cancelarEnvioSesion/<int:sesionId>', views.cancelarEnvioSesion, name="cancelarEnvioSesion"),

    path('ejerciciosSesion/<int:idSesion>', views.ejerciciosSesion, name="ejerciciosSesion"),


]

