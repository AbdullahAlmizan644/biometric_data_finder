# Generated by Django 3.2.18 on 2023-06-04 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_alter_persondata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondata',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
