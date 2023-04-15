from django import forms 
from.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField, ChoiceField
from django.forms.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import django.forms
import django.forms.utils
import django.forms.widgets

cargos = (
    ("1", "-------------------"),
    ("Gerente de Portifólio de Projetos", "Gerente de Portifólio de Projetos"),
    ("Gerente de Projetos", "Gerente de Projetos"),
    ("Diretor", "Diretor"),
    ("Setor Financeiro", "Setor Financeiro"),
    ("Administrador", "Administrador"),
)
tipo = (
    ("Fornecedor", "Fornecedor"),
    ("Cliente", "Cliente")
)
tipos_de_serviço = (
    ("Desenvolvimento Softwares e Aplicativos", "Desenvolvimento Softwares e Aplicativos"),
    ("Serviços Suporte à Infraestrutura de Software", "Serviços Suporte à Infraestrutura de Software"),
    ("Armazenamento de Dados", "Armazenamento de Dados"),
    ("Proteção de Dados", "Proteção de Dados"),
    ("Segurança Cibernética", "Segurança Cibernética"),
    ("Computação em Nuvem", "Computação em Nuvem"),
)   

situação_projeto = (
    ("Ativo", "Ativo"),
    ("Inativo", "Inativo")
)

situação_user = (
    ("Ativo", "Ativo"),
    ("Inativo", "Inativo")
)

situação_os = (
    ("Ativa", "Ativa"),
    ("Inativa", "Inativa"),
    ("Concluída", "Concluída")
)


class FuncionarioForm(forms.ModelForm):

    cargo = ChoiceField(choices = cargos)
    situação = ChoiceField(choices = situação_user)
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["nome"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'nome',
            'name': 'nome',
            'placeholder': 'Digite aqui'
        })
        self.fields["cpf"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'cpf',
            'name': 'cpf',
            'placeholder': 'Digite aqui'
        })
        self.fields['data_nascimento'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-aaaa (DOB)',
                'class': 'form-control'
                }
            )
        self.fields["endereço"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'endereco',
            'name': 'endereco', 
            'placeholder': 'Digite aqui'
        })
        self.fields["cidade"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'cidade',
            'name': 'cidade', 
            'placeholder': 'Digite aqui'
        })
        self.fields["bairro"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'bairro',
            'name': 'bairro', 
            'placeholder': 'Digite aqui'
        })
        self.fields["cargo"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'cargo',
            'name': 'cargo', 
            'placeholder': 'Escolha'
        })
        self.fields["situação"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'situação',
            'name': 'situação', 
            'placeholder': 'situação'
        })
        
    class Meta:
        model = funcionarios
        fields = ('nome', 'cpf', 'endereço', 'data_nascimento', 'cidade', 'bairro', 'cargo', 'situação')


class credenciais(UserCreationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'nome',
            'name': 'nome',
            'placeholder': 'Digite aqui'
        })
        self.fields["password1"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'password1',
            'name': 'password1',
            'placeholder': 'Digite aqui'
        })
        self.fields["password2"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'password2',
            'name': 'password2',
            'placeholder': 'Digite aqui'
        })        
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Fornecedores_Clientes_Form(forms.ModelForm):

    tipo = ChoiceField(choices = tipo)
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["cpf_cnpj"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'cpf_cnpj',
            'name': 'cpf_cnpj',
            'placeholder': 'Digite aqui'
        })
        self.fields["razão_social"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'razão_social',
            'name': 'razão_social',
            'placeholder': 'Digite aqui'
        })
        self.fields["nome_fantasia"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'nome_fantasia',
            'name': 'nome_fantasia',
            'placeholder': 'Digite aqui'
        })

        self.fields["rg"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'rg',
            'name': 'rg', 
            'placeholder': 'Digite aqui'
        })
        self.fields["endereço"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'endereço',
            'name': 'endereço', 
            'placeholder': 'Digite aqui'
        })
        self.fields["email"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'email',
            'name': 'email', 
            'placeholder': 'Digite aqui'
        })
        self.fields["complemento"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'complemento',
            'name': 'complemento', 
            'placeholder': 'Digite aqui'
        })
        self.fields["tipo"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'tipo',
            'name': 'tipo', 
            'placeholder': 'situação'
        })
        self.fields["pais"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'pais',
            'name': 'pais', 
            'placeholder': 'Digite aqui'
        })
        
    class Meta:
        model = fornecedores_clientes
        fields = ('cpf_cnpj', 'razão_social', 'nome_fantasia', 'rg', 'endereço', 'email', 'complemento', 'tipo', 'pais')


class Projetos_Form(forms.ModelForm):

    situação = ChoiceField(choices = situação_projeto)
    tipo_serviço = ChoiceField(choices = tipos_de_serviço)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["n_contrato"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'n_contrato',
            'name': 'n_contrato',
            'placeholder': 'Digite aqui'
        })
        self.fields["vigencia"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'vigencia',
            'name': 'vigencia',
            'placeholder': 'Ex: 1 ano, 2 anos...'
        })
        self.fields["cnpj_fk"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'cnpj_fk',
            'name': 'cnpj_fk', 
            'placeholder': 'CPF/CNPJ'
        })
        self.fields["contratante"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'orgao',
            'name': 'orgão', 
            'placeholder': 'Ex: CBM, SEFA, BASA...'
        })
        self.fields["pontos_função"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'pf',
            'name': 'pf', 
            'placeholder': 'Ex: 200'
        })
        self.fields["pontos_função_unit"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'pf_unit',
            'name': 'pf_unit', 
            'placeholder': 'Ex: 200'
        })
        self.fields["valor_total"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'valor',
            'name': 'valor', 
            'placeholder': 'R$100.000,00'
        })
        self.fields["qtd_horas_os"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'oesses',
            'name': 'oesses', 
            'placeholder': 'Ex: 100'
        })
        self.fields["valor_os_unit"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'os_unit',
            'name': 'os_unit', 
            'placeholder': 'Ex: R$250,00'
        })
        self.fields["valor_os_total"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'valor_os_total',
            'name': 'valor_os_total', 
            'placeholder': 'R$25.000,00'
        })
        self.fields["valor_global_contrato"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'valorglob',
            'name': 'valorglob', 
            'placeholder': 'R$125.000,00'
        })
        
        self.fields['data_abertura'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'dd-mm-aaaa (DOB)',
                  'class': 'form-control'
            })

        self.fields["GP_responsavel"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'respPJ',
            'name': 'respPJ',
            'placeholder': 'Digite aqui' 
        })
        self.fields["email_GP_responsavel"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'emailrespPJ',
            'name': 'emailrespPJ',
            'placeholder': 'Digite aqui' 
        })
        self.fields["tipo_serviço"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'TipoServ',
            'name': 'TipoServ'
        })
        self.fields["situação"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'situação',
            'name': 'situação', 
            'placeholder': 'situação'
        })
        self.fields["relatorio"].widget.attrs.update({
            'id' : 'relatorio',
            'name': 'relatorio', 
        })      
    class Meta:
        model = projetos
        fields = ('n_contrato', 'vigencia', 'cnpj_fk', 'contratante', 'pontos_função', 'pontos_função_unit', 'valor_total', 'valor_os_total',
                'qtd_horas_os', 'valor_os_unit', 'valor_global_contrato', 'data_abertura', 'GP_responsavel', 'email_GP_responsavel',
                'tipo_serviço', 'situação', 'relatorio')

class OS_Form(forms.ModelForm):

    situação = ChoiceField(choices = situação_os)
    tipo_serviço = ChoiceField(choices = tipos_de_serviço)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["codigo_os"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'OSnumero',
            'name': 'OSnumero',
            'placeholder': 'Ex: OS-Nº2'
        })
        self.fields["n_contrato"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'n_contrato',
            'name': 'n_contrato',
            'placeholder': 'Ex: 01/2023 - SEFA'
        })
        self.fields['abertura'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'dd-mm-aaaa (DOB)',
                  'class': 'form-control'
            })
        self.fields['vencimento'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'dd-mm-aaaa (DOB)',
                  'class': 'form-control'
            })
        self.fields["cnpj_fk"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'cnpj_fk',
            'name': 'cnpj_fk', 
            'placeholder': 'CPF/CNPJ'
        })
        self.fields["contratante"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'contratante',
            'name': 'contratante', 
            'placeholder': 'Ex: CBM, SEFA, BASA...'
        })
        self.fields["pontos_função"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'pf',
            'name': 'pf', 
            'placeholder': 'Ex: 200'
        })
        self.fields["qtd_horas"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'oesses',
            'name': 'oesses', 
            'placeholder': 'Ex: 45'
        })
        self.fields["tipo_serviço"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'TipoServ',
            'name': 'TipoServ'
        })
        self.fields["situação"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'situação',
            'name': 'situação', 
            'placeholder': 'situação'
        })
        self.fields["descrição"].widget.attrs.update({
            'class' : 'form-control',  
            'id' : 'situação',
            'name': 'situação', 
            'placeholder': 'Digite aqui'
        })
                
    class Meta:
        model = ordem_serviço
        fields = ('codigo_os', 'n_contrato', 'abertura',
                'vencimento', 'cnpj_fk', 'contratante', 'pontos_função', 'qtd_horas',
                'tipo_serviço', 'situação', 'descrição')



class Form_Relatorios(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["relatorio"].widget.attrs.update({
            'id' : 'relatorio',
        })

    class Meta:
        model = relatorios
        fields = ('relatorio',)