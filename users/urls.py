from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, index

# ✅ Роутер түзөбүз жана ViewSet кошобуз
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('index/', index, name='index'),
]
