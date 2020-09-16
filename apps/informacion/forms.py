from django.forms import ModelForm
from django import forms
from betterforms.multiform import MultiModelForm
from .models import Tecnico, mdmqUrbana,Beneficiario, Conyuge,Canton, Parroquia, Ubicacion , Tramite,gadpp,stra,Archivo,mdmq,InformeDirectivo,InformeSociologica,InformeSectorial,drone,predio
import datetime


class BeneficiarioModelForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['nombre','apellido','cedula','celular','correo','sexo','edad','dignidad','estado_civil','tramite','conyuge']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'cedula': forms.TextInput(attrs={'placeholder': '1727XXXXX-X'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ejm: 098XXXXXXX'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ejm: XXXX@gmail.com'}),
            'dignidad': forms.TextInput(attrs={'placeholder': 'Ejm: Presidente,Directivo,etc'}),
            'edad': forms.TextInput(attrs={'placeholder': 'Ejm: 23-50,etc'})
        }

 
class TramiteModelForm(ModelForm):
    class Meta:
        model = Tramite
        fields = ['tipo_tramite', 'numero','fecha_reunion_ingreso','fecha_reunion_sector','viavilidad','escritura','plano','irm','copia_cedula','otro','tecnico','parroquia','ubicacion']
        widgets = {
            'fecha_reunion_ingreso': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_reunion_sector': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Ejm: 001-002-003, etc'}),
            'escritura': forms.CheckboxInput(attrs={'class':'form-control'}),
            'plano': forms.CheckboxInput(attrs={'class':'form-control'}),
            'irm': forms.CheckboxInput(attrs={'class':'form-control'}),
            'copia_cedula': forms.CheckboxInput(attrs={'class':'form-control'})
        }
    def clean_fecha(self):
        fecha = self.cleaned_data('fecha_reunion_ingreso')
        if fecha > datetime.date.today():
            raise forms.ValidationError('La fecha no puede ser mayor al dia de hoy')
        return fecha

class IngresoTramiteModelForm(MultiModelForm):
    form_classes = {
        'tramite': TramiteModelForm,
        'beneficiario': BeneficiarioModelForm,
    }
    def save(self, commit=True):
        objects = super(IngresoTramiteModelForm, self).save(commit=False)

        if commit:
            beneficiario = objects['beneficiario']
            beneficiario.save()
            tramite = objects['tramite']
            tramite.save()
        return objects



#seguimiento rural

class gadppModelForm(ModelForm):
    class Meta:
        model = gadpp
        fields = '__all__'
        widgets = {
            'fecha_entrega_plano_borrador': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_firma_plano_original': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
        }
        

class straModelForm(ModelForm):
    class Meta:
        model = stra
        fields = ['fecha_inspeccion','fecha_certificado_mae','fecha_ingreso_stra','fecha_entrega_providencia','numero_providencia','registro_stra','tramite']
        widgets = {
            'fecha_inspeccion': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_certificado_mae': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_ingreso_stra': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_entrega_providencia': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'numero_providencia': forms.TextInput(attrs={'placeholder': 'Ejm:'}),
            'registro_stra': forms.TextInput(attrs={'placeholder': 'Ejm:'})
        }


class mdmqModelForm(ModelForm):
    class Meta:
        model = mdmq
        fields = '__all__'
        widgets = {
            'certificado_estado': forms.TextInput(attrs={'placeholder': 'Ejm: 002bdb'}),
            'fecha_entrega_certificado_estado': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_ingreso_registro_propiedad': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'numero_registro': forms.TextInput(attrs={'placeholder': 'Ejm: '}),
        }

class SeguimientoRuralModelForm(MultiModelForm):
    form_classes = {
        'gadpp': gadppModelForm,
        'stra': straModelForm,
        'mdmq': mdmqModelForm,
    }
    def save(self, commit=True):
        objects = super(SeguimientoRuralModelForm, self).save(commit=False)

        if commit:
            gadpp = objects['gadpp']
            gadpp.save()
            stra = objects['stra']
            stra.save()
            mdmq = objects['mdmq']
            mdmq.save()
        return objects

#Archivo

class archivoModelForm(ModelForm):
    class Meta:
        model = Archivo
        fields = '__all__'
        widgets = {
            'fecha': forms.SelectDateWidget(),
			'razones': forms.Textarea(attrs={'rows':4, 'cols':80,'placeholder': 'Ingrese la Razon del Tramite a Archivar'}),
        }

class ArchivoModelForm(MultiModelForm):
    form_classes = {
        'archivo': archivoModelForm,
    }
    def save(self, commit=True):
        objects = super(ArchivoModelForm, self).save(commit=False)

        if commit:
            archivo = objects['archivo']
            archivo.save()
        return objects

#Informe directivo

class InformeDirectivoModelForm(ModelForm):
    class Meta:
        model = InformeDirectivo
        fields = '__all__'
        widgets = {
            'fecha_entrega_informacion': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_firma_convenio': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'numero_beneficiario_sector': forms.TextInput(attrs={'placeholder': 'Ejm: 1-2-3'}),
            'conf_socialpredio': forms.TextInput(attrs={'placeholder': 'Ejm: '}),
            'problemas_encontrados': forms.Textarea(attrs={'placeholder': 'Prpblemas encontrados','rows':4, 'cols':40}),
            'posibles_soluciones': forms.Textarea(attrs={'placeholder': 'Posibles soluciones','rows':4, 'cols':40})
        }

class conyugeModelForm(ModelForm):
    class Meta:
        model = Conyuge
        fields = '__all__'

class BeneficiarioModelForm(ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['nombre','apellido','cedula','celular','correo','sexo','edad','dignidad','estado_civil','tramite','conyuge']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Ejm: 1727XXXXX-X'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ejm: 098XXXXXXX'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ejm: XXXX@gmail.com'}),
            'dignidad': forms.TextInput(attrs={'placeholder': 'Ejm: Presidente,Directivo,etc'}),
            'edad': forms.TextInput(attrs={'placeholder': 'Ejm: 23-50,etc'})
        }

class ReunionDirectivoModelForm(MultiModelForm):
    form_classes = {
        'informedirectivo': InformeDirectivoModelForm,
        'beneficiario': BeneficiarioModelForm,
    }
    def save(self, commit=True):
        objects = super(ReunionDirectivoModelForm, self).save(commit=False)

        if commit:
            informedirectivo = objects['informedirectivo']
            informedirectivo.save()
            beneficiario = objects['beneficiario']
            beneficiario.save()
        return objects


#seguimientoUrbana

class mdmqUrbanaModelForm(ModelForm):
    class Meta:
        model = mdmqUrbana
        fields = '__all__'
        widgets = {
            'fecha_ingreso_dmq': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_solicitud_cambio': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_reingreso_dmq': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
        }

class SeguimientoUrbanaModelForm(MultiModelForm):
    form_classes = {
        'mdmqurbana': mdmqUrbanaModelForm,
    }
    def save(self, commit=True):
        objects = super(SeguimientoUrbanaModelForm, self).save(commit=False)

        if commit:
            mdmqUrbana = objects['mdmqurbana']
            mdmqUrbana.save()
        return objects
#reunion sectorial sociologica

class InformeSociologicaModelForm(ModelForm):
    class Meta:
        model = InformeSociologica
        fields = '__all__'
        widgets = {
            'fecha_reunion_soci': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'homogenidad_predial': forms.TextInput(attrs={'placeholder': 'Homogeniedad predial'}),
            'def_procesos_intervencion': forms.TextInput(attrs={'placeholder': 'Definicion de procesos'}),
            'datos_predios': forms.Textarea(attrs={'placeholder': 'Datos de predios','rows':4, 'cols':30})
        }

class InformeSociologicoModelForm(MultiModelForm):
    form_classes = {
        'informesociologica': InformeSociologicaModelForm,
        'beneficiario': BeneficiarioModelForm
    }
    def save(self, commit=True):
        objects = super(InformeSociologicoModelForm, self).save(commit=False)

        if commit:
            informesociologica = objects['informesociologica']
            informesociologica.save()
            beneficiario = objects['beneficiario']
            beneficiario.save()
        return objects


#reunion sectorial tecnica


class InformeSectorialModelForm(ModelForm):
    class Meta:
        model = InformeSectorial
        fields = '__all__'
        widgets = {
            'numero': forms.Textarea(attrs={'rows':4, 'cols':5,'placeholder': 'Ejm: 1'}),
            'CoordenadaX': forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder': 'Ejm: -097XXXXXXX'}),
            'CoordenadaY': forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder': 'Ejm: -097XXXXXXX'}),
            'fecha_toma_puntos': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'fecha_reunion_sec': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'numero_beneficiarios': forms.TextInput(attrs={'placeholder': 'Ejm: 1'}),
            'pdo_arranque': forms.TextInput(attrs={'placeholder': 'Ejm: 1'})
        }

class droneModelForm(ModelForm):
    class Meta:
        model = drone
        fields = '__all__'
        widgets = {
            'fecha_vuelo': forms.DateInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'topografia': forms.TextInput(attrs={'placeholder': 'Topografia'}),
            'altura_vuelo': forms.TextInput(attrs={'placeholder': 'Ejm: 100 metros'}),
            'resolucion_gsd': forms.TextInput(attrs={'placeholder': 'Ejm: 6000 px X 4000 px'}),
            'velocidad_vuelo': forms.TextInput(attrs={'placeholder': 'Ejm: 262 km/h'}),
            'angulo_inclinacion': forms.TextInput(attrs={'placeholder': 'Ejm: 30 Grados'}),
        }

class InformeSectorialTecnicaModelForm(MultiModelForm):
    form_classes = {
        'informesectorial': InformeSectorialModelForm,
        'drone': droneModelForm,
    }
    def save(self, commit=True):
        objects = super(InformeSectorialTecnicaModelForm, self).save(commit=False)

        if commit:
            informesectorial = objects['informesectorial']
            informesectorial.save()
            drone = objects['drone']
            drone.save()
        return objects


#informacion del predio


class predioModelForm(ModelForm):
    class Meta:
        model = predio
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.TextInput(attrs={'placeholder': 'dd/mm/yyy'}),
            'coordenadaX': forms.TextInput(attrs={'placeholder': 'Ejm: -0987XXXXX'}),
            'coordenadaY': forms.TextInput(attrs={'placeholder': 'Ejm: -0978XXXXX'}),
            'superficie': forms.TextInput(attrs={'placeholder': 'Ejm: 100mtrs'}),
            'observaciones': forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder': 'Observaciones del predio'})
        }

class InformePredioModelForm(MultiModelForm):
    form_classes = {
        'predio': predioModelForm,
        'beneficiario': BeneficiarioModelForm
    }
    def save(self, commit=True):
        objects = super(InformePredioModelForm, self).save(commit=False)

        if commit:
            predio = objects['predio']
            predio.save()
            beneficiario = objects['beneficiario']
            beneficiario.save()
        return objects

#conyuge

class conyugeModelForm(ModelForm):
    class Meta:
        model = Conyuge
        fields = '__all__'

class ConyugeModelForm(MultiModelForm):
    form_classes = {
        'conyuge': conyugeModelForm,
    }
    def save(self, commit=True):
        objects = super(ConyugeModelForm, self).save(commit=False)

        if commit:
            conyuge = objects['conyuge']
            conyuge.save()
        return objects


