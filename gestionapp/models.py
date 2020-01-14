from django.db import models

# Create your models here.

COLORES = (
    ('0', 'Blanco'),
    ('1', 'Negro'),
    ('2', 'Rojo'),
    ('3', 'Amarillo'),
    ('4', 'Azul'),
)

class Camposcomunes_masterdoc(models.Model):
    codigo = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=30, null=True, blank=True)
    tipdoc = models.CharField(max_length=30, null=True, blank=True)
    destipdoc = models.CharField(max_length=30, null=True, blank=True)
    seriedoc = models.CharField(max_length=30, null=True, blank=True)
    numerodoc = models.CharField(max_length=30, null=True, blank=True)
    fechadoc = models.DateField(null=True, blank=True)
    fecentrega = models.DateField(null=True, blank=True)  # Fecha entrega pedido
    ruc = models.CharField(max_length=30, null=True, blank=True)
    desruc = models.CharField(max_length=150, null=True, blank=True)
    telruc = models.CharField(max_length=30, null=True, blank=True)
    paisruc = models.CharField(max_length=30, null=True, blank=True)
    dptoruc = models.CharField(max_length=30, null=True, blank=True)
    provruc = models.CharField(max_length=30, null=True, blank=True)
    distruc = models.CharField(max_length=30, null=True, blank=True)
    codpostalruc = models.CharField(max_length=30, null=True, blank=True)
    dirruc = models.CharField(max_length=150, null=True, blank=True)
    conpag = models.CharField(max_length=30, null=True, blank=True)
    desconpag = models.CharField(max_length=50, null=True, blank=True)
    monedapago = models.IntegerField(default=0)  # soles,dolares,euros,yen
    desmonepago = models.CharField(max_length=50, null=True, blank=True)
    tc_dolares = models.DecimalField(default=0, max_digits=15, decimal_places=4, null=True, blank=True)
    tc_euros = models.DecimalField(default=0, max_digits=15, decimal_places=4, null=True, blank=True)
    tc_yen = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    numeroguia = models.IntegerField(default=0)
    numordserv = models.IntegerField(default=0)
    vendidopor = models.CharField(max_length=30, null=True, blank=True)
    fechapago = models.DateField(null=True, blank=True)
    unidadtransporte = models.CharField(max_length=50, null=True, blank=True)
    autorizadosunat = models.IntegerField(default=0)
    impsubtotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impanticipos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impdescuentos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impvalorventa = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impisc = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impigv = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    nvaligv = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impotroscargos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impotrostributos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    imptotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    cc1 = models.CharField(max_length=30, null=True, blank=True)  # cc para saber donde se hace gasto
    cc2 = models.CharField(max_length=30, null=True, blank=True)
    cc3 = models.CharField(max_length=30, null=True, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    correoruc = models.CharField(max_length=150, null=True, blank=True)
    horaini = models.CharField(max_length=30, null=True, blank=True)
    horafin = models.CharField(max_length=30, null=True, blank=True)
    lugorigen = models.CharField(max_length=50, null=True, blank=True)
    lugdestino = models.CharField(max_length=50, null=True, blank=True)
    opcviaje = models.CharField(max_length=30, null=True, blank=True)
    grupo = models.CharField(max_length=100, null=True, blank=True)
    obs =  models.TextField(null=True, blank=True)
    comonoscontacto = models.CharField(max_length=150, blank=True, null=True)
    
    class Meta:
        abstract = True


class Camposcomunes_detaildoc(models.Model):
    codigo = models.IntegerField(default=0)
    codpro = models.CharField(max_length=30, null=True, blank=True)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    pax = models.IntegerField(default=0, null=True, blank=True)
    unimed = models.CharField(max_length=60, null=True, blank=True)
    desunimed = models.CharField(max_length=60, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    precio = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impsubtotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impanticipos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impdescuentos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impvalorventa = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impisc = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impigv = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    nvaligv = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impotroscargos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impotrostributos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    imptotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    desgrupo1 = models.CharField(max_length=30, null=True, blank=True)
    desgrupo2 = models.CharField(max_length=30, null=True, blank=True)
    cc1 = models.CharField(max_length=30, null=True, blank=True)  # cc para saber donde se hace gasto
    cc2 = models.CharField(max_length=30, null=True, blank=True)
    cc3 = models.CharField(max_length=30, null=True, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    horaini = models.CharField(max_length=30, null=True, blank=True)
    horafin = models.CharField(max_length=30, null=True, blank=True)
    lugorigen = models.CharField(max_length=50, null=True, blank=True)
    lugdestino = models.CharField(max_length=50, null=True, blank=True)
    opcviaje = models.CharField(max_length=30, null=True, blank=True)
    conductor = models.CharField(max_length=50, null=True, blank=True)
    nombreguia = models.CharField(max_length=50, null=True, blank=True)
    nvuelo = models.CharField(max_length=50, null=True, blank=True)
    proveedor = models.CharField(max_length=50, null=True, blank=True)
    tipodoc = models.CharField(max_length=50, null=True, blank=True)
    obs =  models.TextField(null=True, blank=True)
    #user_tracking
    alert = models.CharField(max_length=50, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    starttask = models.DateTimeField(blank=True, null=True)
    endtask = models.DateTimeField(blank=True, null=True)
    start_longitude = models.FloatField(null=True, blank=True)
    end_longitude = models.FloatField(null=True, blank=True)
    start_latitude = models.FloatField(null=True, blank=True)
    end_latitude = models.FloatField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    signature = models.ImageField(upload_to='user_tracking', null=True, blank=True)
    estadodoc = models.ForeignKey('CotizacionEstado', blank=True, null=True, on_delete=models.CASCADE)
    
    

    class Meta:
        abstract = True


class Camposcomunes_auditoria(models.Model):
    sucursal = models.CharField(max_length=10, blank=True, null=True)
    estado = models.IntegerField(default=0)
    anulado = models.IntegerField(default=0)
    fecregistro = models.DateField(null=True, blank=True)
    aud_idusu = models.CharField(max_length=30, blank=True, null=True)
    aud_feccre = models.DateTimeField(auto_now=True)
    aud_fecmod = models.DateField(null=True, blank=True)
    aud_feceli = models.DateField(null=True, blank=True)
    posmapa = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Camposcomunes_personal(models.Model):
    codigo = models.CharField(max_length=15, blank=True, null=True)
    ruc = models.CharField(max_length=15, null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    telefono2 = models.CharField(max_length=30, blank=True, null=True)
    telefono3 = models.CharField(max_length=30, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telcontacto = models.CharField(max_length=30, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    contacto2 = models.CharField(max_length=100, blank=True, null=True)
    telcontacto2 = models.CharField(max_length=30, blank=True, null=True)
    correo2 = models.CharField(max_length=150, blank=True, null=True)
    contacto3 = models.CharField(max_length=100, blank=True, null=True)
    telcontacto3 = models.CharField(max_length=30, blank=True, null=True)
    correo3 = models.CharField(max_length=150, blank=True, null=True)
    contacto4 = models.CharField(max_length=100, blank=True, null=True)
    telcontacto4 = models.CharField(max_length=30, blank=True, null=True)
    correo4 = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    tipocc = models.IntegerField(default=0, blank=True, null=True)
    destipocc = models.CharField(max_length=100, blank=True, null=True)
    condcompvent = models.CharField(max_length=100, blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100, blank=True, null=True)
    banco_nomdest1 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20, blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100, blank=True, null=True)
    banco_nomdest2 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20, blank=True, null=True)
    banco_nombre3 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta3 = models.CharField(max_length=100, blank=True, null=True)
    banco_nomdest3 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda3 = models.CharField(max_length=20, blank=True, null=True)
    fechanac = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    grupo = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    idioma = models.CharField(max_length=80, blank=True, null=True)
    categprov = models.CharField(max_length=80, blank=True, null=True)
    tipocontrato = models.CharField(max_length=100, blank=True, null=True)
    comonoscontacto = models.CharField(max_length=150, blank=True, null=True)
    class Meta:
        abstract = True


class Deposito(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)


# Unidades de Transporte
class Unidad(models.Model):
    codigo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    placa = models.CharField(max_length=30, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    aniofab = models.IntegerField(default=0, null=True, blank=True)
    npasajeros = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    combustible = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    cadsoat = models.DateField(null=True, blank=True)
    empsoat = models.CharField(max_length=100, blank=True, null=True)
    revtec = models.DateField(null=True, blank=True)
    emprevtec = models.CharField(max_length=100, blank=True, null=True)
    segveh = models.DateField(null=True, blank=True)
    empsegveh = models.CharField(max_length=100, blank=True, null=True)
    mantglp = models.DateField(null=True, blank=True)
    empglp   = models.CharField(max_length=100, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    docbrevete = models.FileField(upload_to='documents/', null=True, blank=True)
    docdni = models.FileField(upload_to='documents/', null=True, blank=True)
    doccursos = models.FileField(upload_to='documents/', null=True, blank=True)
    docantepoli = models.FileField(upload_to='documents/', null=True, blank=True)
    docantepena = models.FileField(upload_to='documents/', null=True, blank=True)
    foto1 = models.ImageField(upload_to='unidad', null=True, blank=True)
    foto2 = models.ImageField(upload_to='unidad', null=True, blank=True)

    # Guias de Turismo
class Guia(Camposcomunes_personal, Camposcomunes_auditoria):
    foto1 = models.ImageField(upload_to='documents/', null=True, blank=True)
    foto2 = models.ImageField(upload_to='documents/', null=True, blank=True)
    foto3 = models.ImageField(upload_to='documents/', null=True, blank=True)
    pass
    
class Articulo(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=60)
    cantidad = models.IntegerField(default=0)
    color = models.CharField(max_length=2, default=0, choices=COLORES)
    deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)
    stock1 = models.IntegerField(default=0)
    codbarra = models.CharField(max_length=60, blank=True, null=True)
    stockalm1 = models.IntegerField(default=0)
    stockalm2 = models.IntegerField(default=0)
    stockalm3 = models.IntegerField(default=0)
    afectoigv = models.IntegerField(default=0)
    preciocosto = models.IntegerField(default=0)
    precioventa = models.IntegerField(default=0)
    aplicadscto = models.IntegerField(default=0)
    cc1 = models.CharField(max_length=60, blank=True, null=True)
    descc1 = models.CharField(max_length=60, blank=True, null=True)


class Banco(models.Model):
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)


# centro de costo para monitor de flujo gasto ingreso


class Cliente(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Proveedor(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Transporte(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Chofer(Camposcomunes_personal, Camposcomunes_auditoria):
    foto1 = models.ImageField(upload_to='documents', null=True, blank=True)
    dnivence = models.DateField(null=True, blank=True)
    cursos =  models.CharField(max_length=150, blank=True, null=True)
    docbrevete = models.FileField(upload_to='documents/', null=True, blank=True)
    brevete = models.CharField(max_length=50, blank=True, null=True)
    brevetevence = models.DateField(null=True, blank=True)
    docdni = models.FileField(upload_to='documents/', null=True, blank=True)
    docpasaporte = models.FileField(upload_to='documents/', null=True, blank=True)
    pass


# ARCHIVOS DE MOVIMIENTO
# mliquidacion no debe existir el encabezado es el detalle de los servicios 



class Mcotizacion(Camposcomunes_masterdoc, Camposcomunes_auditoria):
    pass


class Dcotizacion(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    master = models.ForeignKey(Mcotizacion, related_name='cotizaciones', on_delete=models.CASCADE, null=True)


class Dliquidacion(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    master = models.ForeignKey(Dcotizacion, related_name='liquidaciones', on_delete=models.CASCADE, null=True)


class Mguia(models.Model):
    pass


class Dguia(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    pass


class Mgasto(models.Model):
    pass


class Dgasto(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    pass


class Clientesdireccion(models.Model):
    master = models.ForeignKey(Cliente, related_name='clientesdirecciones', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    class Meta:
        unique_together = ('master', 'id')
        ordering = ['id']

    def __unicode__(self):
        return '%d: %s' % (self.direccion, self.telefono)


class CotizacionEstado(models.Model):
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=100)
