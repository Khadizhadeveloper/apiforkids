from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from users.urls import user_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # API маршруты под /api/
    path('index/', user_list, name='user_list'),  # Шаблонный маршрут
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),
]