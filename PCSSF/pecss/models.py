from django.db import models


class Usuario(models.Model):
    rol = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)  
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.IntegerField()  # Cambiado a IntegerField
    direccion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class Cliente(models.Model):
    tipoDocumento = models.CharField(max_length=50)
    numeroIdentificacion = models.IntegerField()  # Cambiado a IntegerField
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)  # Ajustado a 13 caracteres según la base de datos
    email = models.CharField(max_length=50)  # Ajustado a 50 caracteres según la base de datos
    direecion = models.CharField(max_length=50)  # Corregido el nombre del campo
    estado = models.CharField(max_length=50) 

class Mascota(models.Model):
    fk_ID_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombreMascota = models.CharField(max_length=50)  # Cambiado a nombreMasc
    estado = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    observacion = models.TextField()

class TipoServicio(models.Model):
    tipo_servicio = models.CharField(max_length=50)
    valor_servicio = models.DecimalField(max_digits=10,decimal_places=3)

class Servicio(models.Model):
    fk_id_tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    fk_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    observacion = models.TextField()
    estado = models.CharField(max_length=50)