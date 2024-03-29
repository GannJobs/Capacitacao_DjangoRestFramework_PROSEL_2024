from .views import UsuarioModelViewSet
from rest_framework.routers import DefaultRouter

Urouter = DefaultRouter()
Urouter.register(r'Usuario', UsuarioModelViewSet, basename='usuario')

urlpatterns = Urouter.urls