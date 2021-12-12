from django.shortcuts import render
from . import serializers
from rest_framework import viewsets
from . import models
from rest_framework.response import Response

import datetime

class FornecedoresView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.FornecedorSerializer

class NaturezasDespesaView(viewsets.ModelViewSet):
    queryset = models.NaturezasDespesa.objects.all()
    serializer_class = serializers.NaturezasDespesaSerializer

class SitucoesUsoBemView(viewsets.ModelViewSet):
    queryset = models.SitucoesUsoBem.objects.all()
    serializer_class = serializers.SitucoesUsoBemSerializer

class EstadosBemView(viewsets.ModelViewSet):
    queryset = models.EstadosBem.objects.all()
    serializer_class = serializers.EstadosBemSerializer

class MarcasView(viewsets.ModelViewSet):
    queryset = models.Marcas.objects.all()
    serializer_class = serializers.MarcasSerializer

class NotasFiscaisView(viewsets.ModelViewSet):
    queryset = models.NotasFiscais.objects.all()
    serializer_class = serializers.NotasFiscaisSerializer

class ItensNotaFiscalView(viewsets.ModelViewSet):
    queryset = models.ItensNotaFiscal.objects.all()
    serializer_class = serializers.ItensNotaFiscalSerializer

class BensView(viewsets.ModelViewSet):
    queryset = models.Bens.objects.all()
    serializer_class = serializers.BensSerializer
    