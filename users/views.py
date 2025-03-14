from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render

@extend_schema(tags=["Users"], description="Колдонуучуларды башкаруу API'сы")
class UserViewSet(viewsets.ModelViewSet):
    """
    Колдонуучулар боюнча CRUD API:
    - **GET** /users/ → Бардык колдонуучулар
    - **POST** /users/ → Жаңы колдонуучу кошуу
    - **GET** /users/{id}/ → Белгилүү бир колдонуучу
    - **PUT** /users/{id}/ → Колдонуучуну жаңыртуу
    - **DELETE** /users/{id}/ → Колдонуучуну өчүрүү
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'users/index.html')
