# Generated by Django 2.0.8 on 2019-10-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0046_auto_20190927_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcotizacion',
            name='pax',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='pax',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='pax',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dliquidacion',
            name='pax',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
