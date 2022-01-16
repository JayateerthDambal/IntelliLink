from django.shortcuts import render
from .models import SensorData
from random import uniform
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import SensorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
import json


# Views for  Dashboard
def dash_home(request):
    return render(request, 'dashboard/home.html')


# Ajax request
def dash_getData(request):
    roomTemp = round(uniform(25.5, 28.8), 2)
    loomTemp = round(uniform(29.5, 29.8), 2)
    roomHumid = round(uniform(80.5, 82.5), 2)
    loomHumid = round(uniform(82.6, 83.5), 2)
    request.user.sensordata_set.create(roomTemp=roomTemp, roomHumid=roomHumid, loomHumid=loomHumid, loomtemp=loomTemp,
                                       user=request.user)
    # SensorData.objects.create()
    senseVals = SensorData.objects.values().latest("date_time")
    paramsChartVals = SensorData.objects.filter(user=request.user).values('roomTemp', 'time', 'loomtemp', 'roomHumid',
                                                                          'loomHumid').order_by('-id')[:25][::1]
    # loomHumidVals = SensorData.objects.filter(user=request.user).values('loomHumid', 'time').order_by('-id')[:25][::1]

    return JsonResponse(data={
        'senseVals': senseVals, 'chart_data': paramsChartVals
    })


def humidCharts(request):
    return render(request, 'test.html')


def dash_getHumidData(request):
    humidChartVals = SensorData.objects.filter(user=request.user).values('roomHumid', 'time').order_by('-id')[:25][::1]

    return JsonResponse(data={
        'humidVals': humidChartVals
    })


class SensorDataList(APIView):

    def get(self, request):
        queries = SensorData.objects.all().filter(user=request.user).order_by('-id')[:10]
        serializer = SensorSerializer(queries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # print(request.data['user'])

        serializer = SensorSerializer(data=request.data)
        # print(request.data)

        if serializer.is_valid() and request.user.id == request.data['user']:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



