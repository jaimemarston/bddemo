# Generated by Django 2.0.8 on 2019-06-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_usertraking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertraking',
            old_name='latitude',
            new_name='end_latitude',
        ),
        migrations.RenameField(
            model_name='usertraking',
            old_name='longitude',
            new_name='end_longitude',
        ),
        migrations.AddField(
            model_name='usertraking',
            name='start_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertraking',
            name='start_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
