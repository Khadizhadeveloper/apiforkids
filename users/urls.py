from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, user_list


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
