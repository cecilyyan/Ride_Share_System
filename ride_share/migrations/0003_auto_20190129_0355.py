# Generated by Django 3.0.dev20190125164321 on 2019-01-29 03:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ride_share', '0002_auto_20190129_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 1, 29, 3, 55, 27, 603008, tzinfo=utc), verbose_name='time'),
        ),
    ]
