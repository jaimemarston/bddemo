# Generated by Django 2.0.8 on 2019-08-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0040_auto_20190801_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='foto1',
            field=models.ImageField(blank=True, null=True, upload_to='documents'),
        ),
    ]
