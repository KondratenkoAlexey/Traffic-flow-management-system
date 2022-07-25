# Generated by Django 4.0.6 on 2022-07-24 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_flow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='operator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='traffic_flow.operator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='truck',
            name='warehouse',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1),
        ),
    ]