import jwt
from django.conf import settings
from django.contrib.auth import user_logged_in
from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.utils import jwt_payload_handler

from usuarios.models import Usuarios
from usuarios.models import UserTracking
from usuarios.serializers import AuthenticationUserSerializer, UserTrackingSerializer, UserSerializer, \
    UserTrackingDetailSerializer


class UsertrakingViewSet(viewsets.ModelViewSet):
    serializer_class = UserTrackingSerializer
    queryset = UserTracking.objects.all()


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()

    @action(methods=['GET'], url_path='travels', detail=True, serializer_class=UserTrackingDetailSerializer)
    def get_travels(self, request, pk):
        queryset = UserTracking.objects.filter(user_id=pk).order_by('-id')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class Authenticate(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=False, url_path='obtain_token')
    def obtain_token(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            try:
                user = Usuarios.objects.get(username=username)
                pwd_valid = password == user.password
                if pwd_valid is False:
                    user = None
            except Usuarios.DoesNotExist:
                user = None
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(AuthenticationUserSerializer(user).data,
                                    status=status.HTTP_200_OK)

                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)

        except KeyError:
            res = {'error': 'please provide a email and password'}
            return Response(res)
