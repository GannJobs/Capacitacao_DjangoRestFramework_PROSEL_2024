from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.UserModelViewSet.as_view(), name='usuario'),
]