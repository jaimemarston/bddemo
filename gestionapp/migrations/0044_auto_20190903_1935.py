# Generated by Django 2.0.8 on 2019-09-04 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0043_auto_20190903_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='foto2',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='guia',
            name='foto3',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='guia',
            name='foto1',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
