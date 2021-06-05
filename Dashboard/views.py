from django.shortcuts import render
from .models import SensorData
from random import uniform
from django.http import JsonResponse

# Views for  Dashboard
def dash_home(request):
    return render(request, 'dashboard/home.html')


#### Ajax request
def dash_getData(request):
    roomTemp = round(uniform(25.5,28.8), 3)
    loomTemp = round(uniform(29.5,29.8), 3)
    roomHumid = round(uniform(80.5,82.5), 3)
    loomHumid = round(uniform(82.6,83.5), 3)
    request.user.sensordata_set.create(roomTemp=roomTemp, roomHumid=roomHumid, loomHumid=loomHumid, loomtemp=loomTemp)
    # SensorData.objects.create()
    senseVals =SensorData.objects.values().latest()
    return JsonResponse({'senseVals': senseVals})


