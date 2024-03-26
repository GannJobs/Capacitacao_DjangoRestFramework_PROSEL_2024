# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Tarefa
from .serializer import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import F
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.response import Response
from datetime import datetime

class TarefaModelViewSet(ModelViewSet):
    # authenticacao
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all()

    # Listar tarefas
    def list(self, request):
        taf = Tarefa.objects.all()
        serial = TarefaSerializer(taf, many=True)
        if len(serial.data) > 0:
            return Response({
                'status': 302, 'Tarefa': serial.data
            })
        return Response({'status': 204, 'msg': 'No Content'})

    # criar um usuário
    def create(self, request):
        titulo = request.data.get('titulo')
        desc = request.data.get('descricao')
        data = request.data.get('data_vencimento')
        p = request.data.get('prioridade')
        status = request.data.get('status')
        vinculo = request.user
        Tarefa.objects.create(titulo=titulo,desc=desc, data_vencimento=data, prioridade=p, status=status, vinculo=vinculo)
        return Response({'status': 201, 'msg': 'registered successfully'})

    def update(self, request):
        id = request.data.get('id')
        taf = Tarefa.objects.get(id=id)
        titulo = request.data.get('titulo')
        desc = request.data.get('descricao')
        data = request.data.get('data_vencimento')
        p = request.data.get('prioridade')
        status = request.data.get('status')
        taf.titulo = titulo
        taf.desc = desc
        taf.data_vencimento = data
        taf.prioridade = p
        taf.status = status
        taf.save()
        return super().update(request)

    def delete(self, request):
        id = request.data.get('id')
        taf = Tarefa.objects.get(id=id)
        taf.delete()
        return super().destroy(request)