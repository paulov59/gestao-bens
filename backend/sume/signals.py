from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from . import models


# @receiver(pre_save, sender=models.Fornecedores)
# def teste_pre_save(sender, instance, **kwargs):
#     print('=======================pre save===================')

#     #instance.razao_social = 'pre save'

# @receiver(post_save, sender=models.Fornecedores)
# def teste_post_save(sender, instance, **kwargs):

#     instance.razao_social = 'post save'
#     #instance.save()
