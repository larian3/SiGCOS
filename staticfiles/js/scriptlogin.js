function logar(){
    var login = document.getElementById('login').value;
    var senha = document.getElementById('senha').value;

    /*Função Verificar Login*/
    if (login == 'admin' && senha == 'admin'){
        alert('Logado com Sucesso!');
    }else{
        alert('Usuário ou Senha Incorretos! Tente novamente!');
    }
}