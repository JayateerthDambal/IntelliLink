# Generated by Django 3.2.4 on 2021-11-29 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0004_alter_sensordata_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicIOs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('supplyFan', models.BooleanField()),
                ('returnFan', models.BooleanField()),
                ('loomPump', models.BooleanField()),
                ('roomPump', models.BooleanField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]