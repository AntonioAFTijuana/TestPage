from django.db import models

class GoldenPCBA(models.Model):
    #upload = models.FileField(upload_to = user_directory_path) 
    SerialNumber = models.CharField(max_length=255)
    Customer = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Rev = models.CharField(max_length=50)
    Golden = models.IntegerField()
    Madeby = models.CharField(max_length=255)
    Comments = models.CharField(max_length=255)
    ActiveUnit = models.BooleanField()
    BirthFile = models.FileField(upload_to=None, max_length=254)


class  customer(models.Model):
    CustomerName = models.CharField(max_length=255)
    CustomerID = models.CharField(max_length=255)
    ActiveCustomer = models.IntegerField()

class Accion(models.Model):
    Descripcion = models.CharField(max_length=255)

class CodigosDeFalla(models.Model):
    CodDef = models.CharField(max_length=6)
    Descripcion = models.CharField(max_length=255)

class Defecto(models.Model):
    Codigo = models.CharField(max_length=6)
    Description = models.CharField(max_length=255)

class Diagnostico(models.Model):
    IdTecnico = models.IntegerField()
    FechaPrueba = models.DateTimeField()
    FechaDiagnostico = models.DateTimeField()
    idCliente = models.IntegerField()
    idModelo = models.IntegerField()
    Revision = models.CharField(max_length=255)
    NoSerie = models.CharField(max_length=255)
    Prueba  = models.CharField(max_length=6)
    DescPrueba = models.CharField(max_length=255)
    idDefecto= models.IntegerField()
    Responsable = models.CharField(max_length=255)
    idAccion= models.IntegerField()
    Referencia = models.CharField(max_length=255)
    Tiempo= models.IntegerField()
    Status = models.CharField(max_length=255)
    Comentario = models.CharField(max_length=255)

class Equipo(models.Model):
    NumeroControl = models.CharField(max_length=255)
    IdPropietario  = models.IntegerField()
    IdModelo = models.IntegerField()
    TipoEquipo = models.IntegerField()
    Active = models.IntegerField()

class Inventario(models.Model):
    Serial = models.CharField(max_length=255)
    FechaEntrada = models.DateTimeField()
    FechaSalida = models.DateTimeField()
    Estatus = models.CharField(max_length=255)
    Modelo = models.CharField(max_length=255)
    Revision = models.CharField(max_length=255)
    Cliente = models.CharField(max_length=255)
    SigEstacion = models.CharField(max_length=255)

class LastManto(models.Model):
    IdEquipo= models.IntegerField()
    Date = models.DateTimeField()
    IdManto= models.IntegerField()

class Mantenimiento(models.Model):
    IdEquipo = models.IntegerField()
    MantoDate = models.DateTimeField()
    MantoNextDate = models.DateTimeField()
    IdTechnician= models.IntegerField()
    Comments = models.CharField(max_length=255)
    IdMantoFile= models.IntegerField()

class MantoRegisters(models.Model):
    IdUser = models.IntegerField()
    NombreReporte = models.CharField(max_length=255)
    Date = models.DateTimeField()
    NextDate = models.DateTimeField()

class Modelo(models.Model):
    IdCliente = models.IntegerField()
    Modelo = models.CharField(max_length=255)
    ActiveModel = models.IntegerField(default=True)

class PCEquipo(models.Model):
    IdEquipo = models.IntegerField()
    PCName = models.CharField(max_length=255)

class TiemposMuertos(models.Model):
    Status = models.IntegerField()
    IdEquipo = models.IntegerField()
    Turno = models.IntegerField()
    IdIniciador = models.IntegerField()
    IdTecnico = models.IntegerField()
    Falla = models.CharField(max_length=255)
    HoraInicio = models.DateTimeField()
    HoraTermino = models.DateTimeField()
    IdEnsamble = models.IntegerField()
    Causa = models.CharField(max_length=255)
    Accion = models.CharField(max_length=255,default="")
    HoraTecnico = models.DateTimeField()

class TipoEquipo(models.Model):
    Tipo = models.CharField(max_length=255)

class User(models.Model):
    employeeNumber = models.IntegerField()
    employeeName = models.CharField(max_length=255)
    create = models.BooleanField(default=False)


