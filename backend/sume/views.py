from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from . import models
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

import datetime

class FornecedoresView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.FornecedorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['razao_social']

class NaturezasDespesaView(viewsets.ModelViewSet):
    queryset = models.NaturezasDespesa.objects.all()
    serializer_class = serializers.NaturezasDespesaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['desc_natureza_despesa', 'cod_natureza_despesas']

class SitucoesUsoBemView(viewsets.ModelViewSet):
    queryset = models.SitucoesUsoBem.objects.all()
    serializer_class = serializers.SitucoesUsoBemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['situacao_uso_bem']

class EstadosBemView(viewsets.ModelViewSet):
    queryset = models.EstadosBem.objects.all()
    serializer_class = serializers.EstadosBemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado_bem']
 
class MarcasView(viewsets.ModelViewSet):
    queryset = models.Marcas.objects.all()
    serializer_class = serializers.MarcasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['marca']

class NotasFiscaisView(viewsets.ModelViewSet):
    queryset = models.NotasFiscais.objects.all()
    serializer_class = serializers.NotasFiscaisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'ano']

class ItensNotaFiscalView(viewsets.ModelViewSet):
    queryset = models.ItensNotaFiscal.objects.all()
    serializer_class = serializers.ItensNotaFiscalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['produto_servico', 'vinculado']

class BensView(viewsets.ModelViewSet):
    queryset = models.Bens.objects.all()
    serializer_class = serializers.BensSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_item_nota_fiscal__id_nota_fiscal__id_fornecedor__razao_social']
    
    