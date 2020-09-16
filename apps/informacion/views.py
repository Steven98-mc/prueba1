from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView,ListView

from .forms import IngresoTramiteModelForm, SeguimientoRuralModelForm, SeguimientoUrbanaModelForm,ArchivoModelForm, ReunionDirectivoModelForm,InformeSociologicoModelForm,InformeSectorialTecnicaModelForm,InformePredioModelForm,ConyugeModelForm
from .models import Tecnico, Beneficiario, Canton, Parroquia, Ubicacion , Tramite, gadpp,stra,mdmq,Archivo,mdmqUrbana,InformeSectorial,drone,predio,InformeSociologica

def home(request):
    return render(request,'base.html')

class TramiteCreateView(CreateView):
    form_class = IngresoTramiteModelForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('success')

class TramiteList(ListView):
    model = Tramite  
    template_name = 'lista_tramites.html'

class SeguimientoCreateView(CreateView):
    form_class = SeguimientoRuralModelForm
    template_name = 'seguimiento_rural.html'
    success_url = reverse_lazy('success')

class SeguimientoList(ListView):
    model = gadpp
    template_name = 'lista_seguimiento_rural.html'
class SeguimientostraList(ListView):
    model = stra
    template_name = 'lista_seguimiento_rural2.html'
class SeguimientomdmqList(ListView):
    model = mdmq
    template_name = 'lista_seguimiento_rural3.html'

class SeguimientoUrbanoCreateView(CreateView):
    form_class = SeguimientoUrbanaModelForm
    template_name = 'seguimiento_urbano.html'
    success_url = reverse_lazy('success')

class SeguimientoUrbanoList(ListView):
    model = mdmqUrbana  
    template_name = 'lista_seguimiento_urbana.html'

class ArchivoCreateView(CreateView):
    form_class = ArchivoModelForm
    template_name = 'archivo.html'
    success_url = reverse_lazy('success')

class ArchivoList(ListView):
    model = Archivo
    template_name = 'lista_archivos.html'


class ReunionDirectivosCreateView(CreateView):
    form_class = ReunionDirectivoModelForm
    template_name = 'reunion_directivos.html'
    success_url = reverse_lazy('success')


class InformeSociologicaCreateView(CreateView):
    form_class = InformeSociologicoModelForm
    template_name = 'reunion_sectorial_sociologica.html'
    success_url = reverse_lazy('success')

class ReunionSectorialSociologicaList(ListView):
    model = InformeSociologica
    template_name = 'lista_reunion_sectorial.html'

class InformeSectorialTecnicaCreateView(CreateView):
    form_class = InformeSectorialTecnicaModelForm
    template_name = 'reunion_sectorial_tecnica.html'
    success_url = reverse_lazy('success')

class ReunionSectorialTecnicaList(ListView):
    model = InformeSectorial  
    template_name = 'listar_reunion_sectorial_tecnica.html'
    

class ReunionSectorialTecnicaDroneList(ListView):
    model = drone  
    template_name = 'listar_reunion_sectorial_tecnica2.html'

class InformePredioCreateView(CreateView):
    form_class = InformePredioModelForm
    template_name = 'informacion_predio.html'
    success_url = reverse_lazy('success')

class InformePredioBeneficiarioList(ListView):
    model = Beneficiario  
    template_name = 'lista_informacion_predio.html'

class InformePredioInformePredialList(ListView):
    model = predio
    template_name = 'lista_informacion_predio2.html'

class ConyugeCreateView(CreateView):
    form_class = ConyugeModelForm
    template_name = 'conyuge.html'
    success_url = reverse_lazy('Conyuge_crear')

class SuccessView(TemplateView):
    template_name = 'success.html'
