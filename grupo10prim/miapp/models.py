from django.db import models

# Create your models here.
class Mascota(models.Model):
	nombre = models.CharField(max_length = 300)
	especie = models.CharField(max_length = 200)
	edad = models.IntegerField()
	sexo = models.CharField(max_length = 100)

class ClienteAmo(models.Model):
	nombre = models.CharField(max_length = 300)
	RUT = models.IntegerField()
	telefono = models.IntegerField()
	email = models.EmailField(max_length = 400)
	nombre_usuario = models.CharField(max_length = 100)
	contrasena_usuario = models.CharField(max_length = 100)

class Profesional(models.Model):
	nombre = models.CharField(max_length = 300)
	area = models.CharField(max_length = 100)
	horario = models.CharField(max_length = 200)
	nombre_usuario = models.CharField(max_length = 100)
	contrasena_usuario = models.CharField(max_length = 100)

class SolicitudHora(models.Model):
	tipo_servicio = models.CharField(max_length = 200)
	fecha = models.DateField()
	horario_inicio = models.CharField(max_length = 100)
	horario_final = models.CharField(max_length = 100)

class Atencion(models.Model):
	diagnostico = models.CharField(max_length = 500)
	tratamiento = models.CharField(max_length = 500)

class Producto(models.Model):
	nombre = models.CharField(max_length = 200)
	categoria = models.CharField(max_length = 100)
	marca = models.CharField(max_length = 100)
	cantidad = models.IntegerField()
	disponibilidad = models.IntegerField()
	precio = models.IntegerField()

class Compra(models.Model):
	nombre_cliente = models.CharField(max_length = 300)
	fecha = models.DateField()
	nombre_tarjeta = models.CharField(max_length = 300)
	fecha_tarjeta = models.DateField()
	numero_tarjeta = models.IntegerField()
	cvc_tarjeta = models.IntegerField()
	