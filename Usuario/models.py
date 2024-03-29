from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    Vinculado = models.OneToOneField(User, on_delete=models.CASCADE)
    Telefone = models.CharField(max_length=11, default='00000000000')
    cpf = models.CharField(max_length=11, default='00000000000')
