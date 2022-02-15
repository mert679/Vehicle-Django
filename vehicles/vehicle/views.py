from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

from .models import Vehicles,Switch
from django.template.loader import render_to_string

def index(request):
    all = Vehicles.objects.all()
    return render(request,"vehic/index.html",{
        "all":all
    })

def add(request):
    if request.method =="POST":
        name = request.POST["vname"]
        temperature = request.POST["temperature"]
        avspeed = request.POST["avspeed"]
        speed = request.POST["speed"]
        engine = request.POST["engine"]
        fuel = request.POST["fuel"]
        addVehicle= Vehicles(name=name,engineStatus=engine,fuelLevel=fuel,speed=speed,temperature=temperature,averageSpeed=avspeed)
        addVehicle.save()
        return redirect("/")
    return render(request,"vehic/add.html")

def detail(request,id):
    obj = Vehicles.objects.get(id=id)
    return render(request,"vehic/detail.html",{
        "obj":obj
    })

def update(request,id):
    obj = Vehicles.objects.get(id=id)
    if request.method=="POST":
        obj.name = request.POST["vname"]
        obj.temperature = request.POST["temperature"]
        obj.averageSpeed = request.POST["avspeed"]
        obj.speed = request.POST["speed"]
        obj.engineStatus = request.POST["engine"]
        obj.fuelLevel = request.POST["fuel"]
        obj.save()
        return redirect("/")
    return render(request,"vehic/update.html",{
        "form":obj
    })

def delete(request,id):
    obj = Vehicles.objects.get(id=id)
    obj.delete()
    return redirect("/")


def onOff(request):
    vehicle= get_object_or_404(Switch,id=request.POST.get("veh_id"))#get_object_or_404(Vehicles,id=request.POST.get("id"))
    is_on = True
    context={
        "vehicle":vehicle,
        "is_liked":is_on,

    }
    if request.is_ajax():
        html = render_to_string("vehicle/detail.html",context,request=request)
        return JsonResponse({"form":html})
    return redirect("/")