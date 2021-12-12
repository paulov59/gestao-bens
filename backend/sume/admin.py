from django.contrib import admin
from . import models
from . import actions

class FormularioBase(admin.ModelAdmin):
    readonly_fields = ['id_user_cad','id_user_alt']
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

class FornecedoresForm(FormularioBase):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['razao_social','cnpj','email','telefone']
    list_filter = ['razao_social']
    actions = [actions.atualiza_fornecedores]

admin.site.register(models.Fornecedores, FornecedoresForm)
admin.site.register(models.NaturezasDespesa)
admin.site.register(models.SitucoesUsoBem)
admin.site.register(models.EstadosBem)
admin.site.register(models.Marcas, FormularioBase)
admin.site.register(models.NotasFiscais, FormularioBase)
admin.site.register(models.ItensNotaFiscal, FormularioBase)
admin.site.register(models.Bens, FormularioBase)
