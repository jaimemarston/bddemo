# Generated by Django 2.0.8 on 2019-05-21 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0027_auto_20190410_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dliquidacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('codpro', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True)),
                ('unimed', models.CharField(blank=True, max_length=60, null=True)),
                ('desunimed', models.CharField(blank=True, max_length=60, null=True)),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('precio', models.IntegerField(blank=True, default=0, null=True)),
                ('impsubtotal', models.IntegerField(blank=True, default=0, null=True)),
                ('impanticipos', models.IntegerField(blank=True, default=0, null=True)),
                ('impdescuentos', models.IntegerField(blank=True, default=0, null=True)),
                ('impvalorventa', models.IntegerField(blank=True, default=0, null=True)),
                ('impisc', models.IntegerField(blank=True, default=0, null=True)),
                ('impigv', models.IntegerField(blank=True, default=0, null=True)),
                ('nvaligv', models.IntegerField(blank=True, default=0, null=True)),
                ('impotroscargos', models.IntegerField(blank=True, default=0, null=True)),
                ('impotrostributos', models.IntegerField(blank=True, default=0, null=True)),
                ('imptotal', models.IntegerField(blank=True, default=0, null=True)),
                ('desgrupo1', models.CharField(blank=True, max_length=30, null=True)),
                ('desgrupo2', models.CharField(blank=True, max_length=30, null=True)),
                ('cc1', models.CharField(blank=True, max_length=30, null=True)),
                ('cc2', models.CharField(blank=True, max_length=30, null=True)),
                ('cc3', models.CharField(blank=True, max_length=30, null=True)),
                ('fechaini', models.DateField(blank=True, null=True)),
                ('fechafin', models.DateField(blank=True, null=True)),
                ('horaini', models.CharField(blank=True, max_length=30, null=True)),
                ('horafin', models.CharField(blank=True, max_length=30, null=True)),
                ('lugorigen', models.CharField(blank=True, max_length=50, null=True)),
                ('lugdestino', models.CharField(blank=True, max_length=50, null=True)),
                ('opcviaje', models.CharField(blank=True, max_length=30, null=True)),
                ('conductor', models.CharField(blank=True, max_length=50, null=True)),
                ('nvuelo', models.CharField(blank=True, max_length=50, null=True)),
                ('proveedor', models.CharField(blank=True, max_length=50, null=True)),
                ('tipodoc', models.CharField(blank=True, max_length=50, null=True)),
                ('obs', models.CharField(blank=True, max_length=50, null=True)),
                ('sucursal', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.IntegerField(default=0)),
                ('anulado', models.IntegerField(default=0)),
                ('fecregistro', models.DateField(blank=True, null=True)),
                ('aud_idusu', models.CharField(blank=True, max_length=30, null=True)),
                ('aud_feccre', models.DateTimeField(auto_now=True)),
                ('aud_fecmod', models.DateField(blank=True, null=True)),
                ('aud_feceli', models.DateField(blank=True, null=True)),
                ('posmapa', models.IntegerField(default=0)),
                ('estadodoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionapp.CotizacionEstado')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mliquidacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
                ('tipdoc', models.CharField(blank=True, max_length=30, null=True)),
                ('destipdoc', models.CharField(blank=True, max_length=30, null=True)),
                ('seriedoc', models.CharField(blank=True, max_length=30, null=True)),
                ('numerodoc', models.CharField(blank=True, max_length=30, null=True)),
                ('fechadoc', models.DateField(blank=True, null=True)),
                ('fecentrega', models.DateField(blank=True, null=True)),
                ('ruc', models.CharField(blank=True, max_length=30, null=True)),
                ('desruc', models.CharField(blank=True, max_length=150, null=True)),
                ('telruc', models.CharField(blank=True, max_length=30, null=True)),
                ('paisruc', models.CharField(blank=True, max_length=30, null=True)),
                ('dptoruc', models.CharField(blank=True, max_length=30, null=True)),
                ('provruc', models.CharField(blank=True, max_length=30, null=True)),
                ('distruc', models.CharField(blank=True, max_length=30, null=True)),
                ('codpostalruc', models.CharField(blank=True, max_length=30, null=True)),
                ('dirruc', models.CharField(blank=True, max_length=150, null=True)),
                ('conpag', models.CharField(blank=True, max_length=30, null=True)),
                ('desconpag', models.CharField(blank=True, max_length=50, null=True)),
                ('monedapago', models.IntegerField(default=0)),
                ('desmonepago', models.CharField(blank=True, max_length=50, null=True)),
                ('tc_dolares', models.IntegerField(default=0)),
                ('tc_euros', models.IntegerField(default=0)),
                ('tc_yen', models.IntegerField(default=0)),
                ('numeroguia', models.IntegerField(default=0)),
                ('numordserv', models.IntegerField(default=0)),
                ('vendidopor', models.CharField(blank=True, max_length=30, null=True)),
                ('fechapago', models.DateField(blank=True, null=True)),
                ('unidadtransporte', models.CharField(blank=True, max_length=50, null=True)),
                ('autorizadosunat', models.IntegerField(default=0)),
                ('impsubtotal', models.IntegerField(default=0)),
                ('impanticipos', models.IntegerField(default=0)),
                ('impdescuentos', models.IntegerField(default=0)),
                ('impvalorventa', models.IntegerField(default=0)),
                ('impisc', models.IntegerField(default=0)),
                ('impigv', models.IntegerField(default=0)),
                ('nvaligv', models.IntegerField(default=0)),
                ('impotroscargos', models.IntegerField(default=0)),
                ('impotrostributos', models.IntegerField(default=0)),
                ('imptotal', models.IntegerField(default=0)),
                ('cc1', models.CharField(blank=True, max_length=30, null=True)),
                ('cc2', models.CharField(blank=True, max_length=30, null=True)),
                ('cc3', models.CharField(blank=True, max_length=30, null=True)),
                ('fechaini', models.DateField(blank=True, null=True)),
                ('fechafin', models.DateField(blank=True, null=True)),
                ('correoruc', models.CharField(blank=True, max_length=150, null=True)),
                ('horaini', models.CharField(blank=True, max_length=30, null=True)),
                ('horafin', models.CharField(blank=True, max_length=30, null=True)),
                ('lugorigen', models.CharField(blank=True, max_length=50, null=True)),
                ('lugdestino', models.CharField(blank=True, max_length=50, null=True)),
                ('opcviaje', models.CharField(blank=True, max_length=30, null=True)),
                ('grupo', models.CharField(blank=True, max_length=100, null=True)),
                ('sucursal', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.IntegerField(default=0)),
                ('anulado', models.IntegerField(default=0)),
                ('fecregistro', models.DateField(blank=True, null=True)),
                ('aud_idusu', models.CharField(blank=True, max_length=30, null=True)),
                ('aud_feccre', models.DateTimeField(auto_now=True)),
                ('aud_fecmod', models.DateField(blank=True, null=True)),
                ('aud_feceli', models.DateField(blank=True, null=True)),
                ('posmapa', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dliquidacion',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cotizaciones', to='gestionapp.Mliquidacion'),
        ),
    ]
