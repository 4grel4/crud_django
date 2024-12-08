from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False)
    data_atualizacao = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.nome