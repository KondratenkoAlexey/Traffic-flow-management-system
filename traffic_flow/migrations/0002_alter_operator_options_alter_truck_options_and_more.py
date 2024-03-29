# Generated by Django 4.0.6 on 2022-08-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operator',
            options={'verbose_name': 'Оператор', 'verbose_name_plural': 'Операторы'},
        ),
        migrations.AlterModelOptions(
            name='truck',
            options={'verbose_name': 'Грузовик', 'verbose_name_plural': 'Грузовики'},
        ),
        migrations.AlterField(
            model_name='truck',
            name='company',
            field=models.CharField(max_length=200, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='state',
            field=models.CharField(max_length=1, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_number',
            field=models.CharField(max_length=15, verbose_name='Номер машины'),
        ),
    ]
