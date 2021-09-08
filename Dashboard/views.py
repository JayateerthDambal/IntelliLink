from django.shortcuts import render
from .models import SensorData
from random import uniform
from django.http import JsonResponse


# Views for  Dashboard
def dash_home(request):
    return render(request, 'dashboard/home.html')


#### Ajax request
def dash_getData(request):
    roomTemp = round(uniform(25.5, 28.8), 2)
    loomTemp = round(uniform(29.5, 29.8), 2)
    roomHumid = round(uniform(80.5, 82.5), 2)
    loomHumid = round(uniform(82.6, 83.5), 2)
    request.user.sensordata_set.create(roomTemp=roomTemp, roomHumid=roomHumid, loomHumid=loomHumid, loomtemp=loomTemp,
                                       user=request.user)
    # SensorData.objects.create()
    senseVals = SensorData.objects.values().latest("date_time")
    # roomTempVals = SensorData.objects.values('roomTemp', 'time').order_by('-id')[:10][::1]
    # print(roomTempVals[0]['time'])

    return JsonResponse(data={
        'senseVals': senseVals
    })


def chart_data_rendering(request):
    roomTempvals = SensorData.objects.values('roomTemp', 'time').order_by('-id')[:10][::1]
    # print(type(roomTempvals))
    return JsonResponse({
        'chartVals': roomTempvals
    })
        