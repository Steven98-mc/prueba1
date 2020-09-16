from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import TramiteCreateView, SuccessView,TramiteList, SeguimientoCreateView,SeguimientoUrbanoCreateView,ArchivoCreateView,ReunionDirectivosCreateView,InformeSociologicaCreateView,InformeSectorialTecnicaCreateView,InformePredioCreateView,ArchivoList,SeguimientoList,SeguimientostraList,SeguimientomdmqList,SeguimientoUrbanoList,ReunionSectorialTecnicaList,ReunionSectorialTecnicaDroneList,ConyugeCreateView,InformePredioBeneficiarioList,InformePredioInformePredialList,ReunionSectorialSociologicaList
from . import views


urlpatterns = [
    path('inicio',views.home,name='home page'),
    path('tramite',TramiteCreateView.as_view(), name='Tramite_crear'),
    path('tramite-listar', TramiteList.as_view(), name='Tramite_listar'),
    path('seguimiento', SeguimientoCreateView.as_view(), name='Seguimiento_crear'),
    path('archivo', ArchivoCreateView.as_view(), name='Archivo_crear'),
    path('reunion-directivos', ReunionDirectivosCreateView.as_view(), name='Reunion_Directivos_crear'),
    path('informacion-predio', InformePredioCreateView.as_view(), name='Informacion_Predio_crear'),
    path('informacion-Predio-l', InformePredioBeneficiarioList.as_view(), name='Informacion_Predio_listar'),
    path('informacion-predio-l', InformePredioInformePredialList.as_view(), name='Informacion_predio_listar'),
    path('reunion-sectorial-sociologica', InformeSociologicaCreateView.as_view(), name='Reunion_Sectorial_Sociologica_crear'),
    path('reunion-sectorial', ReunionSectorialSociologicaList.as_view(), name='Reunion_Sectorial_Sociologica_listar'),
    path('reunion-sectorial-tecnica', InformeSectorialTecnicaCreateView.as_view(), name='Reunion_Sectorial_Tecnica_crear'),
    path('reunion-sectorial', ReunionSectorialTecnicaList.as_view(), name='Reunion_Sectorial_Tecnica_listar'),
    path('reunion-sectorial-Drone', ReunionSectorialTecnicaDroneList.as_view(), name='Reunion_Sectorial_Tecnica_drone_listar'),
    path('seguimiento-urbana', SeguimientoUrbanoCreateView.as_view(), name='Seguimiento_Urbana_crear'),
    path('conyuge', ConyugeCreateView.as_view(), name='Conyuge_crear'),
    path('listar-seguimiento-urbana', SeguimientoUrbanoList.as_view(), name='Seguimientourbana_listar'),
    path('listar-archivo', ArchivoList.as_view(), name='Archivo_listar'),
    path('listar-seguimiento', SeguimientoList.as_view(), name='Seguimiento_listar'),
    path('listar-seguimiento2', SeguimientostraList.as_view(), name='Seguimientostra_listar'),
    path('listar-seguimiento3', SeguimientomdmqList.as_view(), name='Seguimientomdmq_listar'),
    path('success/', SuccessView.as_view(), name='success'),
]