from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'mliquidacion', views.LiquidacionViewSet)
router.register(r'mcotizacion', views.CotizacionViewSet)

router.register(r'cotizacion_estado', views.CotizacionEstadoViewSet)

urlpatterns = [
    url(r'^deposito$', views.DepositoList.as_view()),
    url(r'^deposito/(?P<pk>[0-9]+)$', views.DepositoDetail.as_view()),
    url(r'^articulo$', views.ArticuloList.as_view()),
    url(r'^articulo/(?P<pk>[0-9]+)$', views.ArticuloDetail.as_view()),

    url(r'^cliente$', views.ClienteList.as_view()),
    url(r'^cliente/uploadfiles$', views.ClienteUploadFile.as_view()),
    url(r'^cliente/(?P<pk>[0-9]+)$', views.ClienteDetail.as_view()),
    url(r'^clientemasivo$', views.masivo_list),

    url(r'^proveedor$', views.ProveedorList.as_view()),
    url(r'^proveedor/(?P<pk>[0-9]+)$', views.ProveedorDetail.as_view()),

    url(r'^useractivo$', views.UnidadList.as_view()),

    url(r'^unidad$', views.UnidadList.as_view()),
    url(r'^unidad/(?P<pk>[0-9]+)$', views.UnidadDetail.as_view()),

    url(r'^chofer$', views.ChoferList.as_view()),
    url(r'^chofer/(?P<pk>[0-9]+)$', views.ChoferDetail.as_view()),

    url(r'^guia$', views.GuiaList.as_view()),
    url(r'^guia/(?P<pk>[0-9]+)$', views.GuiaDetail.as_view()),

    url(r'^dcotizacion$', views.DcotizacionList.as_view()),
    url(r'^dcotizacion/(?P<pk>[0-9]+)$', views.DcotizacionDetail.as_view()),
    
    url(r'^dliquidacion$', views.DliquidacionList.as_view()),
    url(r'^dliquidacion/(?P<pk>[0-9]+)$', views.DliquidacionDetail.as_view()),

    url(r'^clientesdireccion$', views.ClientesDireccionlist.as_view()),
    url(r'^clientesdirecciondetail$', views.ClientesDireccionlistdetail.as_view()),
    url(r'^', include(router.urls)),

    url(r'^banco$', views.BancoList.as_view()),
    url(r'^generate_pdf$', views.GeneratePDFCotizacionesDetail.as_view()),
    
    url(r'^print_pdf_embajada/(?P<pk>(\d+))/$',views.GeneratePDFEmbajadaDetail.as_view()), 
    #url(r'^generate_pdf/(?P<pk>\d+)/(?P<user>\d+)$', views.GeneratePDFCotizacionesDetail.as_view()),
    #url(r'^generate_pdf/(?P<pk>(\d+))/(?P<user>(\d+))/$',views.GeneratePDFCotizacionesDetail.as_view()), 
    url(r'^generate_pdf/(?P<pk>(\d+))/$',views.GeneratePDFCotizacionesDetail.as_view()), 
    #url(r'^generate_pdf/(?P<pk>\d+)/$', views.GeneratePDFCotizacionesDetail.as_view()),
    url(r'^generate_html$', TemplateView.as_view(template_name="gestionapp/invoice.html")),

    #1 Listas de pantalla
    url(r'^export_xls_clientes$', views.export_xls_clientes, name='clientes'),
    url(r'^export_xls_proveedores$', views.export_xls_proveedores, name='proveedores'),
]
