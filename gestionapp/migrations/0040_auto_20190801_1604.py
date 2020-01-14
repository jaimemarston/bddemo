# Generated by Django 2.0.8 on 2019-08-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0039_auto_20190722_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='chofer',
            name='brevetevence',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chofer',
            name='cursos',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='chofer',
            name='dnivence',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chofer',
            name='docbrevete',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='chofer',
            name='docdni',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='chofer',
            name='docpasaporte',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
