# Generated by Django 3.2.4 on 2021-08-23 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_sensordata_date_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensordata',
            options={'get_latest_by': 'date_time'},
        ),
    ]