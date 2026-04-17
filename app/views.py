from rest_framework import viewsets, generics, filters
from app.models import Product, Categoria
from app.serializers import ProductSerializer, CategoriaSerializer, ListaCategoriaSerializer, ListaProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



"""
Implemente os ViewSets para os modelos, indicando seu respectivo serializer. 
Adicione os ViewSets aos routers para que eles possam ser acessados através das URLs da API.
"""

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria', 'preco']
    search_fields = ['nome']



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("id")
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




    