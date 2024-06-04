from django.contrib import admin
from .models import customer, Accion,Defecto ,Diagnostico,Equipo,Inventario,LastManto,Mantenimiento,MantoRegisters,Modelo,PCEquipo,TiemposMuertos,TipoEquipo,User,GoldenPCBA



class GoldenAdmin(admin.ModelAdmin):
    list_display = ("Customer","Model","Rev","SerialNumber","Madeby")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("CustomerName","CustomerID","ActiveCustomer")

class AccionAdmin(admin.ModelAdmin):
    list_display = ("id","Descripcion")

class DefectoAdmin(admin.ModelAdmin):
    list_display = ("Codigo","Description")

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ("FechaPrueba","FechaDiagnostico","NoSerie","Prueba","DescPrueba","Responsable","Referencia","Tiempo","Status","Comentario")

class EquipoAdmin(admin.ModelAdmin):
    list_display = ("NumeroControl","TipoEquipo","Active")

class InventarioAdmin(admin.ModelAdmin):
    list_display = ("Serial","FechaEntrada","FechaSalida","Estatus","Modelo","Revision","Cliente","SigEstacion")

class LastMantoAdmin(admin.ModelAdmin):
    list_display = ("IdEquipo","Date","IdManto")

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ("IdEquipo","MantoDate","MantoNextDate","IdTechnician","Comments","IdMantoFile")

class MantoRegistersAdmin(admin.ModelAdmin):
    list_display = ("IdUser","NombreReporte","Date","NextDate")

class ModeloAdmin(admin.ModelAdmin):
    list_display = ("Modelo","ActiveModel")

class PCEquipoAdmin(admin.ModelAdmin):
    list_display = ("IdEquipo","PCName")

class TiemposMuertosAdmin(admin.ModelAdmin):
    list_display = ("Status","Turno","Falla","HoraInicio","HoraTermino","Causa","Accion","HoraTecnico")

class TipoEquipoAdmin(admin.ModelAdmin):
    list_display = ("id","Tipo")

class UserAdmin(admin.ModelAdmin):
    list_display = ("employeeNumber","employeeName")




# Register your models here.
admin.site.register(customer,CustomerAdmin)#,Accion)
admin.site.register(Accion,AccionAdmin)
admin.site.register(Defecto,DefectoAdmin)
admin.site.register(Diagnostico,DiagnosticoAdmin)
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Inventario,InventarioAdmin)
admin.site.register(LastManto,LastMantoAdmin)
admin.site.register(Mantenimiento,MantenimientoAdmin)
admin.site.register(MantoRegisters,MantoRegistersAdmin)
admin.site.register(Modelo,ModeloAdmin)
admin.site.register(PCEquipo,PCEquipoAdmin)
admin.site.register(TiemposMuertos,TiemposMuertosAdmin)
admin.site.register(TipoEquipo,TipoEquipoAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(GoldenPCBA,GoldenAdmin)