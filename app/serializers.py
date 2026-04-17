from rest_framework import serializers
from app.models import Categoria, Product

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'categoria', 'imagem', 'criado_em' ,'atualizado_em']




class ListaProductSerializer(serializers.ModelSerializer):
    produto = serializers.ReadOnlyField(source='produto.descricao')
    fields = '__all__'
    class Meta: 
        model = Product
    def get_product(self, obj):
        return obj.get_product_display()
    



class ListaCategoriaSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.descricao')
    fields = '__all__'
    class Meta: 
        model = Categoria
    def get_categoria(self, obj):
        return obj.get_categoria_display()
    
