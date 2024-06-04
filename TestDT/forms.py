from django import forms
from .models import customer,PCEquipo,User,Modelo

#customersid = customer.objects.filter(customer.ActiveCustomer==1)

class CreateNewModel(forms.Form):
    nombreModelo = forms.CharField(label="Numero de parte",max_length=50)
    idCliente = forms.IntegerField(label ="ID de Cliente",)
    modelActive = forms.BooleanField(label ="Activo")