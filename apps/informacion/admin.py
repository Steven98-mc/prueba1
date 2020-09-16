from django.contrib import admin

from apps.informacion.models import Tecnico, mdmqUrbana,Beneficiario,Conyuge, Canton, Parroquia, Ubicacion , Tramite,InformeDirectivo,InformeSociologica,InformeSectorial,drone,predio,gadpp,stra,mdmq,Archivo

# Register your models here.

admin.site.register(Tecnico)
admin.site.register(Beneficiario)
admin.site.register(Conyuge)
admin.site.register(Canton)
admin.site.register(Parroquia)
admin.site.register(Ubicacion)
admin.site.register(Tramite)
admin.site.register(InformeDirectivo)
admin.site.register(InformeSociologica)
admin.site.register(InformeSectorial)
admin.site.register(drone)
admin.site.register(predio)
admin.site.register(gadpp)
admin.site.register(stra)
admin.site.register(mdmq)
admin.site.register(Archivo)
admin.site.register(mdmqUrbana)
