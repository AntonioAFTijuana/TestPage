from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import customer,PCEquipo,User,Modelo
from .forms  import CreateNewModel
# Create your views here.



def home(request):
    custom = customer.objects.all()
    return render(request,'home.html',{'custom': custom})

def equipos(request):
    title1 = 'TestEt1'
    PCs = PCEquipo.objects.all()
    return render(request,'pcequipos.html',{'t':title1,'pc': PCs})

def users(request):
    users = User.objects.all()
    return render(request, 'users.html',{
        'users': users
    })

def Model(request):
    models = Modelo.objects.all()
    return render(request,"Models/Model.html", {'models': models})

def Create_Model(request):
    if request.method == 'GET':
        return render(request,"Create_Model.html", {'form':CreateNewModel()})
    else:
         Modelo.objects.create(IdCliente = request.POST["idCliente"],Modelo = request.POST['nombreModelo'],ActiveModel=True)
         return redirect("../Model/")

