# Generated by Django 2.0.8 on 2018-09-24 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0007_dcotizacion_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcotizacion',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cotizaciones', to='gestionapp.Mcotizacion'),
        ),
    ]
