from django.contrib import admin
from .models import SensorData, BasicIO
# Register your models here.

admin.site.register(SensorData)
admin.site.register(BasicIO)