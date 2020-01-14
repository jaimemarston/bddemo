from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from usuarios.views import Authenticate
from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'authenticate', Authenticate),
router.register(r'usertracking', views.UsertrakingViewSet),
urlpatterns = [
    url(r'^', include(router.urls)),
]
