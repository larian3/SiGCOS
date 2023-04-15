from django.contrib.auth.models import AbstractUser
from django.db import models


#tabela funcionarios
class funcionarios(models.Model):

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=20)
    endereço = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    data_nascimento = models.CharField(max_length=20)
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    situação = models.CharField(max_length=10)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
#tabela para fornecedor que tambem pode ser um cliente e vice-versa
class fornecedores_clientes (models.Model):
    cpf_cnpj=models.CharField(max_length=255)
    razão_social=models.CharField(max_length=255)
    nome_fantasia=models.CharField(max_length=255)
    rg=models.CharField(max_length=255)
    endereço=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    complemento=models.CharField(max_length=255)
    tipo=models.CharField(max_length=255)
    pais=models.CharField(max_length=255)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razão_social

#tabela dos projetos
class projetos(models.Model):

    n_contrato = models.CharField(max_length=100)
    cnpj_fk = models.CharField(max_length=100)
    contratante = models.CharField(max_length=100)
    pontos_função = models.CharField(max_length=100)
    pontos_função_unit = models.CharField(max_length=100)
    valor_total = models.CharField(max_length=100)
    qtd_horas_os = models.CharField(max_length=100)
    valor_os_unit = models.CharField(max_length=100)
    valor_global_contrato = models.CharField(max_length=100)
    data_abertura = models.CharField(max_length=100)
    GP_responsavel = models.CharField(max_length=100)
    email_GP_responsavel = models.CharField(max_length=100)
    vigencia=models.CharField(max_length=100)
    valor_os_total = models.CharField(max_length=100)

    situação = models.CharField(max_length=100)
    tipo_serviço = models.CharField(max_length=100)

    relatorio = models.FileField(upload_to='uploads')

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.contratante
    
    
#tabela para ordem de serviço
class ordem_serviço(models.Model):

    codigo_os = models.CharField(max_length=100)
    n_contrato = models.CharField(max_length=100)
    abertura = models.CharField(max_length=100)
    vencimento = models.CharField(max_length=100)
    cnpj_fk = models.CharField(max_length=100)
    contratante = models.CharField(max_length=100)
    pontos_função = models.CharField(max_length=100)
    qtd_horas = models.CharField(max_length=100)
    tipo_serviço = models.CharField(max_length=100)
    situação = models.CharField(max_length=20)
    descrição = models.CharField(max_length=500)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_os
    

class relatorios(models.Model):

    relatorio = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.relatorio