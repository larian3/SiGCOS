from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from login.autentic import group_required
from django.views.generic import TemplateView
from .forms import *
from .models import funcionarios, projetos, ordem_serviço
import datetime

#================================= VIEWS FINANCEIRO ======================================================

@group_required("setor_financeiro","Diretor")
def lista_fornecedores(request):
    lista_fornecedores_clientes = fornecedores_clientes.objects.filter(tipo = "Fornecedor") 
    return render(request, 'financeiro/lista_fornecedores.html', {'lista_fornecedores_clientes': lista_fornecedores_clientes})


@group_required("setor_financeiro","Diretor")
def lista_clientes(request):
    lista_fornecedores_clientes = fornecedores_clientes.objects.filter(tipo = "Cliente") 
    return render(request, 'financeiro/lista_clientes.html', {'lista_fornecedores_clientes': lista_fornecedores_clientes})


@group_required("setor_financeiro", "Diretor")
def view_cliente(request, id):
    
    cliente = get_object_or_404(fornecedores_clientes, pk=id)
    form_cliente = Fornecedores_Clientes_Form(instance = cliente)

    #VERIFICAÇÃO DE GRUPO DE USUARIO PARA PERMITIR EDIÇÃO DE FORMULARIOS
    def is_financeiro(user):
        return user.groups.filter(name='setor_financeiro').exists()
    
    if (request.method == "POST"):
        
        form_cliente = Fornecedores_Clientes_Form(request.POST, instance = cliente) 
        
        if form_cliente.is_valid() and is_financeiro(request.user):
            form_cliente.save()
            return redirect('lista_clientes')
        else:
            return redirect(autentic_necessaria)
    else:
        return render(request, 'financeiro/cliente.html', {'form_cliente':form_cliente, 'cliente' : cliente})
    

@group_required("setor_financeiro", "Diretor")
def view_fornecedor(request, id):
   
    fornecedor = get_object_or_404(fornecedores_clientes, pk=id)
    form_fornecedor = Fornecedores_Clientes_Form(instance = fornecedor)

    #VERIFICAÇÃO DE GRUPO DE USUARIO PARA PERMITIR EDIÇÃO DE FORMULARIOS
    def is_financeiro(user):
        return user.groups.filter(name='setor_financeiro').exists()

    if (request.method == "POST"):
        form_fornecedor = Fornecedores_Clientes_Form(request.POST, instance = fornecedor) 

        if form_fornecedor.is_valid() and is_financeiro(request.user):
            form_fornecedor.save()
            return redirect('lista_fornecedores')
        
        else:
            return redirect(autentic_necessaria)
    else:
        return render(request, 'financeiro/fornecedor.html', {'form_fornecedor':form_fornecedor, 'fornecedor' : fornecedor})
    

@group_required("setor_financeiro")
def cadastro_financeiro(request):

    #VERIFICAÇÃO DE GRUPO DE USUARIO PARA PERMITIR EDIÇÃO DE FORMULARIOS
    def is_financeiro(user):
        return user.groups.filter(name='setor_financeiro').exists()

    if request.method == 'POST':
        form_cf = Fornecedores_Clientes_Form(request.POST)
       
        if form_cf.is_valid() and is_financeiro(request.user) :
            form_cf.save()
            return redirect(cadastro_financeiro)
        
        else:
            return redirect(autentic_necessaria)
    else:
        form_cf = Fornecedores_Clientes_Form()

    return render(request, 'financeiro/financeiro.html', {'form_cf': form_cf})


#================================= VIEWS LOGIN E USUARIOS ======================================================

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('tela_inicial')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'projetos/login.html', {'form_login': form_login})


@group_required("administrador")
def lista_usuarios(request):
    lista_usuarios = funcionarios.objects.all() 
    return render(request, 'projetos/lista_usuarios.html', {'lista_usuarios': lista_usuarios})

@group_required("administrador")
def view_usuario(request, id):
   
    usuario = get_object_or_404(funcionarios, pk=id)
    form_usuario = FuncionarioForm(instance = usuario)
    
    #VERIFICAÇÃO DE GRUPO DE USUARIO PARA PERMITIR EDIÇÃO DE FORMULARIOS
    def is_adm(user):
        return user.groups.filter(name='administrador').exists()

    if (request.method == "POST"):
        
        form_usuario = FuncionarioForm(request.POST, instance = usuario) 
        
        if form_usuario.is_valid() and is_adm(request.user):
            form_usuario.save()
            return redirect(lista_usuarios)
        else:
            return redirect(autentic_necessaria)
    else:
        return render(request, 'projetos/usuario.html', {'form_usuario':form_usuario, 'usuario' : usuario})


@group_required("administrador")
def cadastrar_info_usuarios(request):

    #VERIFICAÇÃO DE GRUPO DE USUARIO PARA PERMITIR EDIÇÃO DE FORMULARIOS
    def is_adm(user):
        return user.groups.filter(name='administrador').exists()

    if request.method == 'POST':
        
        form_user = FuncionarioForm(request.POST)
        form_credenciais = credenciais(request.POST)
        
        if form_user.is_valid() and form_credenciais.is_valid() and is_adm(request.user):
            form_user.save()
            form_credenciais.save()
            return redirect(lista_usuarios)
        else:
            return redirect(autentic_necessaria)
    else:
        form_credenciais = credenciais()
        form_user = FuncionarioForm()
    return render(request, 'projetos/teste_cadastro_user.html', {'form_usuario': form_credenciais, 'form_user':form_user})


#================================= VIEWS PROJETOS =======================================================

@group_required("gerente_projeto")
def tela_projetos_GP(request):
    lista_projetos = projetos.objects.filter(GP_responsavel=request.user)
    return render(request, 'gerente_projetos/lista_projetos.html',{'lista_projetos': lista_projetos} )


@group_required("gerente_portifolio","diretor")
def tela_projetos(request):
    lista_projetos_gpp = projetos.objects.all()
    return render(request, 'gerente_portifolio/lista_projetos_gpp.html',{'lista_projetos_gpp': lista_projetos_gpp} )


@group_required("gerente_portifolio", "gerente_projeto")
def cadastro_projetos(request):
    if request.method == 'POST':
        form_cadastro_projetos = Projetos_Form(request.POST, request.FILES)

        if form_cadastro_projetos.is_valid() :
            print ("valido")
            form_cadastro_projetos.save()
            return redirect(tela_projetos)
        else:
            return redirect(tela_inicial)
    else:
        form_cadastro_projetos = Projetos_Form()

    return render(request, 'gerente_portifolio/cadastro_projeto.html', {'form_cadastro_projetos': form_cadastro_projetos})


@group_required("gerente_projeto", "administrador", "gerente_portifolio", "diretor")
def view_projeto(request, id):
  
    projeto = get_object_or_404(projetos, pk=id)
    form_projeto = Projetos_Form(instance = projeto)
    
    #VERIFICAÇÃO DE GRUPO DE USUARIO PARA PERMITIR EDIÇÃO DE FORMULARIOS
    def is_gpp(user):
        return user.groups.filter(name='gerente_portifolio').exists()
    
    def is_gp(user):
        return user.groups.filter(name='gerente_projeto').exists()

    if (request.method == "POST"):
        
        form_projeto = Projetos_Form(request.POST, request.FILES, instance = projeto) 
        
        if form_projeto.is_valid() and is_gp(request.user):
            form_projeto.save()
            return redirect('tela_projetos_GP')
        
        elif form_projeto.is_valid() and is_gpp(request.user):
            form_projeto.save()
            return redirect('tela_projetos')
        
        else:
             return redirect(autentic_necessaria)
    
    else:
        return render(request, 'projetos/projeto.html', {'form_projeto':form_projeto, 'projeto' : projeto})
    
    
    


#================================= VIEWS OS ======================================================

@group_required("gerente_projeto")
def cadastro_os(request):
    if request.method == 'POST':
        form_os = OS_Form(request.POST)

        if form_os.is_valid() :
            print ("valido")
            form_os.save()
            return redirect(cadastro_os)
        else:
            return redirect(tela_inicial)
    else:
        form_os = OS_Form()

    return render(request, 'gerente_projetos/cadastrar_os.html', {'form_os': form_os})


@group_required("gerente_projeto")
def view_os(request, id):
    print("aqui")
    os = get_object_or_404(ordem_serviço, pk=id)
    form_os = OS_Form(instance = os)
    
    if (request.method == "POST"):
        
        form_os = OS_Form(request.POST, instance = os) 
        
        if form_os.is_valid():
            form_os.save()
            return redirect('lista_os')
        else:
            return render(request, 'gerente_projetos/os.html', {'form_os':form_os, 'os' : os})
    else:
        return render(request, 'gerente_projetos/os.html', {'form_os':form_os, 'os' : os})

@group_required("gerente_projeto")
def lista_os(request):
    lista_os = ordem_serviço.objects.all()

    filtro = request.GET.get('filtro')
    
    if filtro:
        lista_os = ordem_serviço.objects.filter(Ativa = filtro)
    
    else:
        return render(request, 'gerente_projetos/lista_os.html', {'lista_os': lista_os})



#================================= OUTRAS VIEWS ======================================================

def tela_inicial(request):

    return render(request, 'projetos/inicio.html')


def tela_dashboards(request):

    os_FinalizadosRecentes = ordem_serviço.objects.filter(situação='Concluída', atualizado_em__gt = datetime.datetime.now()-datetime.timedelta(days=30)).count()
    os_Finalizadas = ordem_serviço.objects.filter(situação='Concluída').count()
    os_Pendentes = ordem_serviço.objects.filter(situação='Ativa').count()
    os_inativas= ordem_serviço.objects.filter(situação='Inativa').count()
   
    prjetos_finalizados_recentes = projetos.objects.filter(situação='Concluído', atualizado_em__gt = datetime.datetime.now()-datetime.timedelta(days=30)).count()
    projetos_finalizados = projetos.objects.filter(situação='Concluído').count()
    projetos_pendentes = projetos.objects.filter(situação='Ativo').count()
    projetos_inativos= projetos.objects.filter(situação='Inativo').count()
    
    valor_projetos = projetos.objects.raw("SELECT 1 as id, valor_global_contrato, n_contrato FROM login_projetos where situação = 'Ativo'")
   
    
    return render(request, 'gerente_portifolio/dashboards.html', {'valor_projetos':valor_projetos, 'os_FinalizadosRecentes':os_FinalizadosRecentes,
                                                                'os_Finalizadas':os_Finalizadas,'os_Pendentes':os_Pendentes, 'os_inativas':os_inativas,
                                                                'prjetos_finalizados_recentes': prjetos_finalizados_recentes, 'projetos_finalizados':projetos_finalizados,
                                                                'projetos_pendentes':projetos_pendentes, 'projetos_inativos': projetos_inativos })
 



def autentic_necessaria(request):

    return render(request, 'projetos/autentic_necessaria.html',)



def teste_upload(request):

    if request.method == 'POST':
        form_relatorios = Form_Relatorios(request.POST, request.FILES)

        if form_relatorios.is_valid() :
            print ("valido")
            form_relatorios.save()
            return redirect(tela_projetos)
        else:
            return redirect(tela_inicial)
    else:
        form_relatorios = Form_Relatorios()

    return render(request, 'projetos/upload_relatorio.html', {'form_relatorios': form_relatorios})
