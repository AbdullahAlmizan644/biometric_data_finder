# Generated by Django 3.2.18 on 2023-06-04 07:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 4, 7, 5, 7, 156901, tzinfo=utc)),
        ),
    ]
