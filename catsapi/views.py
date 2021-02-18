import requests
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from catsapi.models import Cat
from catsapi.serializers import CreateUserSerializer, CatSerializer, LoginUserSerializer
from catsbackend.settings import CLIENT_ID, CLIENT_SECRET


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post('http://localhost:8000/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data['username'],
                              'password': request.data['password'],
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        r = requests.post('http://localhost:8000/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': serializer.state_user.username,
                              'password': request.data['password'],
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())
    return Response(serializer.errors)


class CatView(ListModelMixin, CreateModelMixin, GenericAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CatViewDetail(RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewEdit(UpdateAPIView, DestroyAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['write']
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
