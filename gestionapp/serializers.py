from rest_framework import serializers

from gestionapp.models import Deposito, Articulo, Cliente, Proveedor, Unidad, Chofer, Guia, Mcotizacion, Dcotizacion, \
    Dliquidacion,Clientesdireccion, Banco, CotizacionEstado

class Base64ImageField(serializers.ImageField):
    
    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
        
class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ('id', 'codigo', 'descripcion')


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ('id', 'codigo', 'descripcion')


class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'codigo', 'descripcion',
                  'cantidad', 'color', 'deposito')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        #fields = ('id', 'codigo', 'nombre', 'ruc',
        #          'telefono1', 'telefono2', 'telefono3',
        #          'contacto', 'telcontacto','correo',
        #          'contacto2', 'telcontacto2','correo2',
        #          'contacto3', 'telcontacto3','correo3',
        #          'direccion', 'paginaweb', 'tipocc', 'destipocc',
        #          'banco_nombre1', 'banco_cuenta1','banco_nomdest1','banco_moneda1',
        #          'banco_nombre2', 'banco_cuenta2','banco_nomdest2','banco_moneda2',
        #          'fechanac', 'fechaini', 'fechafin', 'grupo', 'pais', 'idioma', 'categprov')

    def create(self, validated_data):
        last_id = Cliente.objects.last().id if Cliente.objects.last() else 1
        validated_data['codigo'] = str(last_id).zfill(6)  # is not None

        return Cliente.objects.create(**validated_data)
    

"""
    def create(self, validated_data):
      #  validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6)
      validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6) if Cliente.objects.last().id  is not None else str(1)
      return Cliente.objects.create(**validated_data)
"""


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'codigo', 'nombre', 'ruc',
                   'telefono1', 'telefono2', 'telefono3',
                   'contacto', 'telcontacto','correo',
                   'contacto2', 'telcontacto2','correo2',
                   'contacto3', 'telcontacto3','correo3',
                   'direccion', 'paginaweb', 'tipocc', 'destipocc',
                   'banco_nombre1', 'banco_cuenta1','banco_nomdest1','banco_moneda1',
                   'banco_nombre2', 'banco_cuenta2','banco_nomdest2','banco_moneda2',
                   'banco_nombre3', 'banco_cuenta3','banco_nomdest3','banco_moneda3',
                   'fechanac', 'fechaini', 'fechafin', 'grupo', 'pais', 'idioma', 'categprov')


    def create(self, validated_data):
        last_id = Proveedor.objects.last().id if Proveedor.objects.last() else 1
        validated_data['codigo'] = str(last_id).zfill(6)  # is not None

        return Proveedor.objects.create(**validated_data)


"""
    def create(self, validated_data):
      #  validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6)
      validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6) if Cliente.objects.last().id  is not None else str(1)
      return Cliente.objects.create(**validated_data)
"""


class DliquidacionSerializer(serializers.ModelSerializer):
     class Meta:
         model = Dliquidacion
         fields = ('id', 'codigo', 'codpro', 'descripcion', 'unimed', 'desunimed', 'cantidad', 'precio', 'impsubtotal',
                   'impanticipos', 'impdescuentos',
                   'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                   'desgrupo1', 'desgrupo2', 'lugorigen', 'lugdestino', 'opcviaje',
                   'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'conductor', 'nvuelo',
                   'proveedor', 'obs', 'tipodoc', 'estado', 'estadodoc', 'posmapa', 'master' )


class DcotizacionSerializer(serializers.ModelSerializer):
    signature = Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    class Meta:
        model = Dcotizacion
        fields = ('id', 'codigo', 'codpro', 'descripcion', 'pax', 'unimed', 'desunimed', 'cantidad', 'precio', 'impsubtotal',
                  'impanticipos', 'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'desgrupo1', 'desgrupo2', 'lugorigen', 'lugdestino', 'opcviaje',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'conductor', 'nombreguia', 'nvuelo',
                  'proveedor', 'obs', 'tipodoc', 'estado', 'estadodoc', 'posmapa', 'master',
                  'alert', 'detail', 'is_active', 'creation_date', 'update_date', 'starttask', 'endtask', 'start_longitude',
                  'end_longitude', 'start_latitude', 'end_latitude', 'rating', 'signature' )

   

class McotizacionSerializer(serializers.ModelSerializer):
    cotizaciones = DcotizacionSerializer(many=True, read_only=True)

    class Meta:
        model = Mcotizacion
        fields = ('id', 'codigo', 'descripcion', 'tipdoc', 'destipdoc', 'seriedoc', 'numerodoc', 'fechadoc',
                  'fecentrega', 'ruc', 'desruc', 'telruc', 'paisruc', 'dptoruc', 'provruc', 'distruc', 'codpostalruc',
                  'dirruc', 'conpag', 'desconpag', 'monedapago', 'desmonepago', 'tc_dolares', 'tc_euros', 'tc_yen',
                  'numeroguia', 'numordserv', 'vendidopor', 'fechapago', 'autorizadosunat', 'impsubtotal',
                  'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'correoruc', 'unidadtransporte',
                  'lugorigen', 'lugdestino', 'opcviaje',
                  'estado', 'grupo', 'posmapa','obs','comonoscontacto', 'cotizaciones')

class MliquidacionSerializer(serializers.ModelSerializer):
    #liquidaciones = DliquidacionSerializer(many=True, read_only=True)
    liquidaciones = DcotizacionSerializer(many=True, read_only=True)
    class Meta:
        model = Dcotizacion
        fields = ('id', 'codigo', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'lugorigen', 'lugdestino', 'opcviaje',
                  'estado', 'liquidaciones')


class ClientesdireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientesdireccion
        fields = ('direccion', 'telefono')
        # fields = '__all__'


class ClientesdirecciondetalleSerializer(serializers.ModelSerializer):
    clientesdirecciones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cliente
        fields = ('nombre', 'ruc', 'clientesdirecciones')


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = '__all__'


class CotizacionEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionEstado
        fields = '__all__'
