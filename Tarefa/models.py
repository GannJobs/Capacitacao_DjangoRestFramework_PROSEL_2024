from django.db import models
from Usuario.models import Usuario
# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_digits=20, default='Vazio')
    desc = models.CharField(max_digits=100, default='Sem conteúdo')
    data_vencimento = models.DateField()
    prioridade = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    vinculo = models.ForeignKey(Usuario, on_delete=models.CASCADE)