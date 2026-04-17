from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.




class Categoria(models.Model):
    """
        nome: Nome da categoria. Campo obrigatório, com no máximo 100 caracteres.

        descricao: Descrição breve da categoria. Campo opcional, com no máximo 500 caracteres.

        criado_em: Data e hora de criação da categoria. Campos automáticos gerados pelo sistema.

        atualizado_em: Data e hora da última atualização da categoria. Campos automáticos gerados pelo sistema.
    """
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=500, blank=True)
    criado_em = models.DateField(auto_now=True)
    atualizado_em = models.DateField(auto_now_add=True)



class Product(models.Model):
    """
    Modelo de Produto:
        nome: Nome do produto. Campo obrigatório, com no máximo 255 caracteres.

        descricao: Descrição detalhada do produto. Campo opcional, com no máximo 1000 caracteres.

        preco: Preço do produto. Campo obrigatório, deve ser um número decimal positivo.

        quantidade_estoque: Quantidade disponível em estoque. Campo obrigatório, deve ser um número inteiro positivo.

        categoria: Chave estrangeira para o modelo Categoria. Campo obrigatório, deve ser uma categoria existente no sistema.

        imagem: Campo opcional para armazenar a URL da imagem do produto. Campo opcional, deve ser uma URL válida para uma imagem.

        criado_em: Data e hora de criação do produto. Campos automáticos gerados pelo sistema.

        atualizado_em: Data e hora da última atualização do produto. Campos automáticos gerados pelo sistema.
    """

    nome = models.CharField(max_length=255, null=False)
    descricao = models.CharField(max_length= 1000, blank=True)
    preco = models.DecimalField(max_length=10, max_digits=5, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagem = models.URLField(blank=True, null= True)
    criado_em = models.DateTimeField(auto_now=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)
    