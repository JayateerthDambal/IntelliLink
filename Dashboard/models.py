from django.db import models
from django.contrib.auth.models import  User

# Sensor Model

class SensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    ###SensorValues
    roomTemp = models.FloatField(max_length=10, null=True)
    roomHumid = models.FloatField(max_length=10, null=True)
    loomHumid = models.FloatField(max_length=10, null=True)
    loomtemp = models.FloatField(max_length=10, null=True)


    class Meta:
        get_latest_by = 'date_time'


class BasicIO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)


    ## Basic IOs
    supplyFan = models.BooleanField()
    returnFan  = models.BooleanField()
    loomPump = models.BooleanField()
    roomPump = models.BooleanField()
