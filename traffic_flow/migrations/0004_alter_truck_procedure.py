# Generated by Django 4.0.6 on 2022-07-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_flow', '0003_alter_truck_departure_time_alter_truck_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='procedure',
            field=models.CharField(max_length=10),
        ),
    ]
