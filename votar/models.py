import datetime
from time import timezone
from django.db import models

# Create your models here.

class Questao(models.Model):
    # Campo de caracteres com tamanho máximo
    questao_texto = models.CharField(max_length=200)
    pub_data = models.DateField('data_publicacao')

    # Modo de apresentação da informação, no mínimo para o shell
    def __str__(self):
        return self.questao_texto

    # Verifica se questão foi criada recentemente, 1 dia
    def publicado_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
        # Bool
 

class Escolha(models.Model):
    # Toda alternativa tem que estar vinculada a uma pergunta
    # É isso que a chave estrangeira faz, e ao ser deletada uma pergunta as alternativas ligadas a pergunta serão apagadas também. 
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=200)
    # Campo de número inteiro
    # Valor padrão zero
    votos = models.IntegerField(default=0)

    # Modo de apresentação da informação, no mínimo para o shell
    def __str__(self):
        return self.escolha_texto
