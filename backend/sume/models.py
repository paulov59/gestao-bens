from django.db import models
from django.contrib.auth.models import User

class DadosCadModel(models.Model):
    id_user_cad = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='%(class)s_user_cad'
    )
    
    dt_cad = models.DateField(
        auto_now_add=True
    )
    
    id_user_alt = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,blank=True,
        related_name='%(class)s_user_alt'
    
    )
    
    dt_alt = models.DateField(
        null=True,
        blank=True,
        auto_now=True
    )

    class Meta:
        abstract = True

class Fornecedores(DadosCadModel):
    id_fornecedor = models.AutoField(
        primary_key=True
    )
    
    razao_social = models.CharField(
        null=False,
        max_length=60
    )
    
    cnpj = models.CharField(
        max_length=30,
        unique=True
    )
    
    email = models.CharField(
        max_length=60,
        unique=True
    )
    
    telefone = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )
    
    class Meta:
        ordering = [
            'razao_social'
        ]
        db_table = 'Fornecedores'
        verbose_name_plural = 'Fornecedores'

    def __str__(self) -> str:
        return self.razao_social 

class NaturezasDespesa(models.Model):
    id_natureza_despesa = models.AutoField(
        primary_key=True
    )
    
    cod_natureza_despesas = models.CharField(
        max_length=8
    )
    
    desc_natureza_despesa = models.CharField(
        max_length=60
    )

    class Meta:
        ordering = [
            'desc_natureza_despesa'
        ]
        db_table = 'NaturezasDespesa'
        verbose_name_plural = 'Naturezas Despesas'

    def __str__(self) -> str:
        return self.desc_natureza_despesa

class SitucoesUsoBem(models.Model):
    class SitucaoUsoBem(models.TextChoices):
        emUso = 'EM USO'
        cautela = 'EM CAUTELA'
        manutencao = 'EM MANUTENÇÂO'
        disponivel = 'EM DISPONIBILIDADE'
        aguardandoRecolhimento = 'AGUARDANDO RECOLHIMENTO'
        recolhido = 'RECOLHIDO'
        
    id_situacao_uso_bem = models.AutoField(
        primary_key=True
    )
    
    situacao_uso_bem = models.CharField(
        max_length=80,
        choices=SitucaoUsoBem.choices
    )
    
    descricao = models.CharField(
        max_length=255
    )
    
    ativo = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = [
            'situacao_uso_bem'
        ]
        db_table = 'SituacoesUsoBem'
        verbose_name_plural = 'Situações de Uso'

    def __str__(self) -> str:
        return self.descricao

class EstadosBem(models.Model):
    class EstadoBem(models.TextChoices):
        bom = 'BOM'
        regular = 'REGULAR'
        precario = 'PRECÁRIO'
        antieconomico = 'ANTIECONÔMICO'
        inservivel = 'INSERSÍVEL'
        
    id_estado_bem = models.AutoField(
        primary_key=True
    )

    estado_bem = models.CharField(
        max_length=80,
        choices=EstadoBem.choices
    )

    descricao = models.CharField(
        max_length=255
    )
    
    ativo = models.BooleanField(
        default=True
    )
    
    class Meta:
        ordering = [
            'estado_bem'
        ]
        db_table = 'EstadosBem'
        verbose_name_plural = 'Estado do Bem'
    
    def __str__(self) -> str:
        return self.descricao

class Marcas(DadosCadModel):
    id_marca = models.AutoField(
        primary_key=True
    )
    
    marca = models.CharField(
        max_length=80
    )
    
    class Meta:
        ordering = [
            'marca'
        ]
        db_table = 'Marcas'
        verbose_name_plural = 'Marcas'

    def __str__(self) -> str:
        return self.marca

class NotasFiscais(DadosCadModel):
    id_nota_fiscal = models.AutoField(
        primary_key=True
    )
    
    id_fornecedor = models.ForeignKey(
        Fornecedores,
        on_delete=models.Case
    )
    
    id_natureza_despesa = models.ForeignKey(
        NaturezasDespesa,
        on_delete=models.Case
    )
    
    numero = models.IntegerField()
    
    ano = models.IntegerField()
        
    class Meta:
        ordering = [
            'numero'
        ]
        db_table = 'NotasFiscais'
        verbose_name_plural = 'Notas Fiscais'
    
    def __str__(self) -> str:
        return self.id_fornecedor.razao_social + "-" + str(self.numero) +'/'+str(self.ano)
    
    def numeroAno(self) -> str:
        return str(self.numero) +'/'+str(self.ano)

class ItensNotaFiscal(DadosCadModel):
    id_item_nota_fiscal = models.AutoField(
        primary_key=True
    )
    
    id_nota_fiscal = models.ForeignKey(
        NotasFiscais,
        on_delete=models.CASCADE
    )
    
    qtd = models.IntegerField()
    
    valor_unitario = models.FloatField()
    
    produto_servico = models.CharField(
        max_length=100
    )
    
    vinculado = models.BooleanField(
        default=True
    )
    
    
    class Meta:
        ordering = [
            'produto_servico'
        ]
        db_table = 'ItensNotaFiscal'
        verbose_name_plural = 'Itens das notas fiscais'
    
    def __str__(self) -> str:
        return str(self.id_nota_fiscal) + "-" + self.produto_servico

class Bens(DadosCadModel):
    id_bem = models.AutoField(
        primary_key=True
    )
    
    id_item_nota_fiscal = models.ForeignKey(
        ItensNotaFiscal,
        on_delete=models.Case
    )
    
    tombamento = models.CharField(
        max_length=10
    )
    
    id_estado_bem = models.ForeignKey(
        EstadosBem,
        on_delete=models.Case
    )

    id_situacao_uso_bem = models.ForeignKey(
        SitucoesUsoBem,
        on_delete=models.Case
    )
    
    valor_aquisicao = models.FloatField()
    
    id_marca = models.ForeignKey(
        Marcas,
        on_delete=models.Case
    )

    data_lim_garantia = models.DateField()

    data_fim_garantia = models.DateField()

    data_inicio_uso = models.DateField()
    
    observacoes = models.TextField(
        blank=True,
        null=True
    )


    class Meta:
        ordering = [
            'tombamento'
        ]
        db_table = 'Bens'
        verbose_name_plural = 'Bens'

    def __str__(self) -> str:
        return self.id_item_nota_fiscal.produto_servico + '/' + self.tombamento