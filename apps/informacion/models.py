from django.db import models


# Create your models here.

class Tecnico(models.Model):
    nombres_tec = models.CharField(max_length=20)
    apellidos_tec = models.CharField(max_length=20)
    puesto_tec = models.CharField(max_length=20)

    def __str__(self):
        txt = "Tecnico : {0} {1}"
        return txt.format(self.nombres_tec , self.apellidos_tec)

class Canton(models.Model):
    nombre_canton= models.CharField(max_length=20)
    cod_canton = models.CharField(max_length=20)
    def __str__(self):
        txt = "Canton : {0}"
        return txt.format(self.nombre_canton )

class Parroquia(models.Model):
    nombre_parroquia= models.CharField(max_length=20)
    cod_parroquia = models.CharField(max_length=20)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0} Parroquia {1}"
        return txt.format(self.canton , self.nombre_parroquia)

class Ubicacion(models.Model):
    sector= models.CharField(max_length=100)
    canton = models.OneToOneField(Canton, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Sector :{0} "
        return txt.format(self.sector)

class Tramite(models.Model):
    TIPO_TRAMITE =(
        ('0','Adjudicacion Individual'),
        ('1','Adjudicacion Colectiva'),
        ('2','Actualizacion catastral'),
        ('3','Levantamiento Predial'),
        ('4','Otros')
    )
    tipo_tramite = models.CharField(choices=TIPO_TRAMITE, max_length=2)
    numero = models.CharField(max_length=20,)
    fecha_reunion_ingreso = models.DateField()
    fecha_reunion_sector = models.DateField()
    Viavilidad = (
        ('0','SI'),
        ('1','NO')
    )
    viavilidad = models.CharField(choices=Viavilidad,max_length=1)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    escritura = models.BooleanField(blank=True)
    plano = models.BooleanField(blank=True)
    irm = models.BooleanField(blank=True)
    copia_cedula = models.BooleanField(blank=True)
    otro = models.CharField(max_length=50,blank=True)



    def __str__(self):
        txt = "Tramite : {0} "
        return txt.format(self.numero )

class Conyuge(models.Model):
    nombre_conyuge = models.CharField(max_length=25)
    apellido_conyuge = models.CharField(max_length=25)
    cedula_connyugue = models.CharField(max_length=13)

    def __str__(self):
        txt = " {0} {1} "
        return txt.format(self.nombre_conyuge, self.apellido_conyuge )

class Beneficiario(models.Model):
    nombre= models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    cedula = models.CharField(max_length=13)
    celular = models.CharField(max_length=25)
    correo = models.EmailField(max_length=50)
    Sexo=(
        ('M','Masculino'),
        ('F','Femenino')
    )
    sexo = models.CharField(choices=Sexo,max_length=2,default='M')
    dignidad = models.CharField(max_length=30)
    edad = models.CharField(max_length=3)
    Estado_civil=(
        ('0','Soltero'),
        ('1','Casado'),
        ('2','Divorciado'),
        ('3','Viudo'),
        ('4','Union Libre')
    )
    estado_civil = models.CharField(choices=Estado_civil,max_length=5,default='0')
    conyuge = models.OneToOneField(Conyuge,on_delete=models.CASCADE,null=True,blank=True)
    tramite = models.ForeignKey(Tramite,on_delete=models.CASCADE,blank=True,null=True)



class InformeDirectivo(models.Model):
    fecha_entrega_informacion = models.DateField()
    fecha_firma_convenio = models.DateField()
    numero_beneficiario_sector = models.CharField(max_length=20)
    problemas_encontrados = models.CharField(max_length=1000)
    posibles_soluciones = models.CharField(max_length=1000)
    conf_socialpredio = models.CharField(max_length=1000)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)

class InformeSociologica(models.Model):
    fecha_reunion_soci = models.DateField()
    homogenidad_predial = models.CharField(max_length=1000)
    datos_predios = models.CharField(max_length=1000)
    def_procesos_intervencion = models.CharField(max_length=1000)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)


class InformeSectorial(models.Model):
    fecha_reunion_sec = models.DateField()
    fecha_toma_puntos = models.DateField()
    numero = models.CharField(max_length=10)
    CoordenadaX = models.CharField(max_length=100)
    CoordenadaY = models.CharField(max_length=100)
    pdo_arranque = models.CharField(max_length=13)
    numero_beneficiarios = models.CharField(max_length=13)
    tecnico = models.ForeignKey(Tecnico, null=True,blank=True, on_delete=models.CASCADE)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)


class drone(models.Model):
    fecha_vuelo = models.DateField()
    topografia = models.CharField(max_length=100)
    resolucion_gsd = models.CharField(max_length=100)
    altura_vuelo = models.CharField(max_length=50)
    velocidad_vuelo = models.CharField(max_length=50)
    angulo_inclinacion = models.CharField(max_length=50)
    tecnico = models.ForeignKey(Tecnico, null=True,blank=True, on_delete=models.CASCADE)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)



class gadpp(models.Model):
    fecha_entrega_plano_borrador = models.DateField()
    fecha_firma_plano_original = models.DateField()
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)

class stra(models.Model):
    fecha_inspeccion = models.DateField()
    fecha_certificado_mae = models.DateField()
    fecha_ingreso_stra = models.DateField()
    fecha_entrega_providencia = models.DateField()
    numero_providencia = models.CharField(max_length=10)
    registro_stra = models.CharField(max_length=20)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)

class mdmqUrbana(models.Model):
    fecha_ingreso_dmq = models.DateField()
    fecha_solicitud_cambio = models.DateField()
    fecha_reingreso_dmq = models.DateField()
    tecnico = models.ForeignKey(Tecnico, null=True,blank=True, on_delete=models.CASCADE)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)


class mdmq(models.Model):
    certificado_estado = models.CharField(max_length=20)
    fecha_entrega_certificado_estado = models.DateField()
    fecha_ingreso_registro_propiedad = models.DateField()
    numero_registro = models.CharField(max_length=20)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)

class Archivo(models.Model):
    fecha = models.DateField()
    razones = models.CharField(max_length=1000)
    tecnico = models.ForeignKey(Tecnico, null=True,blank=True, on_delete=models.CASCADE)
    tramite = models.OneToOneField(Tramite,on_delete=models.CASCADE)

    def __str__(self):
        txt = "Archivo : {0} / Razon: {1} {2}"
        return txt.format(self.fecha , self.razones, self.tecnico)

class predio(models.Model):
    fecha_ingreso = models.DateField()
    coordenadaX = models.CharField(max_length=50)
    coordenadaY = models.CharField(max_length=50)
    superficie = models.CharField(max_length=50)
    geocodigo = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=1000)
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE)
