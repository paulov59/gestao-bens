from rest_framework import serializers
from . import models


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedores
        fields = '__all__' # ['id_projeto',"titulo"]

class NaturezasDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NaturezasDespesa
        fields = '__all__' # ['id_projeto',"titulo"]

class SitucoesUsoBemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SitucoesUsoBem
        fields = '__all__' # ['id_projeto',"titulo"]

class EstadosBemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EstadosBem
        fields = '__all__' # ['id_projeto',"titulo"]

class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marcas
        fields = '__all__' # ['id_projeto',"titulo"]

class NotasFiscaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotasFiscais
        fields = '__all__' # ['id_projeto',"titulo"]

class ItensNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensNotaFiscal
        fields = '__all__' # ['id_projeto',"titulo"]

class BensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bens
        fields = '__all__' # ['id_projeto',"titulo"]