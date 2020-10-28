from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    nome = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    dataentrada = models.DateTimeField((), auto_now=False, auto_now_add=False)
    foto = models.ImageField()
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)
    
    class meta:
        db_table = 'pet'
    



