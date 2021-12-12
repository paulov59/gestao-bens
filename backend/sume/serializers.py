from rest_framework import serializers
from . import models


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedores
        fields = '__all__' # ['id_projeto',"titulo"]
            
    def to_representation(self, obj):
        user_cad = 'null'
        if obj.id_user_cad:
            user_cad = obj.id_user_cad.username
        user_alt = 'null'
        if obj.id_user_alt:
            user_alt = obj.id_user_alt.username
        
        return {
		"id_fornecedor": obj.id_fornecedor,
		"dt_cad": obj.dt_cad,
		"dt_alt": obj.dt_alt,
		"razao_social": obj.razao_social,
		"cnpj": obj.cnpj,
		"email": obj.email,
		"telefone": obj.telefone,
		"id_user_cad": user_cad,
		"id_user_alt": user_alt
	}

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
    def to_representation(self, obj):
        user_cad = 'null'
        if obj.id_user_cad:
            user_cad = obj.id_user_cad.username
        user_alt = 'null'
        if obj.id_user_alt:
            user_alt = obj.id_user_alt.username
        
        return {
            "marca": obj.marca,
            "user_cad": user_cad,
            "user_alt": user_alt
        }

class NotasFiscaisSerializer(serializers.ModelSerializer):
    #id_fornecedor = FornecedorSerializer()
    
    class Meta:
        model = models.NotasFiscais
        fields = '__all__' # ['id_projeto',"titulo"]

    def to_representation(self, obj):
        user_cad = 'null'
        if obj.id_user_cad:
            user_cad = obj.id_user_cad.username
        user_alt = 'null'
        if obj.id_user_alt:
            user_alt = obj.id_user_alt.username

        return {
            "id_nota_fiscal": obj.id_nota_fiscal,
            "data cadastro": obj.dt_cad,
            "data alteração": obj.dt_alt,
            "numero": obj.numero,
            "ano": obj.ano,
            "usuário de cadastro": user_cad,
            "usuário que alterou": user_alt,
            "id_fornecedor": obj.id_fornecedor.razao_social,
            "id_natureza_despesa": obj.id_natureza_despesa.desc_natureza_despesa
	    }

class ItensNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensNotaFiscal
        fields = '__all__' # ['id_projeto',"titulo"]
    def to_representation(self, obj):
        user_cad = 'null'
        if obj.id_user_cad:
            user_cad = obj.id_user_cad.username
        user_alt = 'null'
        if obj.id_user_alt:
            user_alt = obj.id_user_alt.username
        return {
            "id_item_nota_fiscal": obj.id_item_nota_fiscal,
            "dt_cad": obj.dt_cad,
            "dt_alt": obj.dt_alt,
            "qtd": obj.qtd,
            "valor_unitario": obj.valor_unitario,
            "produto_servico": obj.produto_servico,
            "vinculado": obj.vinculado,
            "id_user_cad": user_cad,
            "id_user_alt": user_alt,
            "id_nota_fiscal": obj.id_nota_fiscal.numeroAno()
        }

class BensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bens
        fields = '__all__' # ['id_projeto',"titulo"]
        
    def to_representation(self, obj):
        user_cad = 'null'
        if obj.id_user_cad:
            user_cad = obj.id_user_cad.username
        user_alt = 'null'
        if obj.id_user_alt:
            user_alt = obj.id_user_alt.username
        
        return 	{
            "número": obj.tombamento,
            "prestador": obj.id_item_nota_fiscal.id_nota_fiscal.id_fornecedor.razao_social,
            "nota fiscal": obj.id_item_nota_fiscal.id_nota_fiscal.numeroAno(),
            "valor": obj.valor_aquisicao,
            "observacoes": "",
            "id_user_cad": user_cad,
            "id_user_alt": user_alt,
        }