from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('inicio/', tela_inicial, name = 'tela_inicial'),
    #path('login/', tela_login.as_view(), name = 'tela_login'),
    #path('GPP/', views.projetos_GPP, name='projetos_GPP'),
   # path('GP/', views.projetos_GP, name='projetos_GP'),
    path('financeiro/', cadastro_financeiro, name='financeiro'),
    #path('cadastrousuarios/', views.cadastro_ADM, name='cadastro_ADM'),
    #path('cadastrar_usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    #path('lista_projetos/', tela_projetos_GP, name = "tela_projetos_GP"),
    path('cadastrar_projeto/', cadastro_projetos, name = "cadastrar_projeto"),

   # path('atualizar_projeto/', atualizar_projeto, name = "atualizar_projeto"),

    path('logar_usuario/', logar_usuario, name = "logar_usuario"),
    path('autentic_necessaria/', autentic_necessaria, name = "autentic_necessaria"),
    path('teste_cadastro_user/', cadastrar_info_usuarios, name = "teste_cadastro_user"),
    path('lista_fornecedores/', lista_fornecedores, name = "lista_fornecedores"),
    path('fornecedor/<int:id>', view_fornecedor, name = 'view_fornecedor'),
    path('lista_clientes/', lista_clientes, name = "lista_clientes"),
    path('cliente/<int:id>', view_cliente, name = 'view_cliente'),    
    path('lista_usuarios/', lista_usuarios, name = "lista_usuarios"),
    path('usuario/<int:id>', view_usuario, name = 'view_usuario'),    

    path('lista_projetos_gpp/', tela_projetos, name = "tela_projetos"),
    path('lista_projetos_GP/', tela_projetos_GP, name = "tela_projetos_GP"),

    path('projeto/<int:id>', view_projeto, name = 'view_projeto'),
    path('cadastro_os/', cadastro_os, name = 'cadastro_os'),
    path('lista_os/', lista_os, name = "lista_os"),
    path('os/<int:id>', view_os, name = 'view_os'),

    path('upload_relatorio/', teste_upload, name= "upload_relatorio"),
    path('tela_dashboards/', tela_dashboards, name = 'tela_dashboards'),
]



