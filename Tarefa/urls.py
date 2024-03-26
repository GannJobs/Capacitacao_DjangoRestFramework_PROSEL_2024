from django.urls import path
from . import views

urlpatterns = [
    path('tarefa/', views.TarefaModelViewSet.as_view(), name='tarefa'),
]