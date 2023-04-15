const form = document.getElementById("formUser");
const nome = document.getElementById("nome");
const cpf = document.getElementById("cpf");
const data_nasc = document.getElementById("data_nasc");
const endereco = document.getElementById("endereco");
const cidade = document.getElementById("cidade");
const bairro = document.getElementById("bairro");
const cargo = document.getElementById("cargo_selecionado");
const situacao_atv = document.getElementById("gridRadios1");
const situacao_inat = document.getElementById("gridRadios2");
const email = document.getElementById("email");
const senha = document.getElementById("senha");

var btnAdd = document.querySelector("#btnAdd");

//Botão Adicionar;
btnAdd.addEventListener("click", function(event){
    //Evita o carregamento da página;
    event.preventDefault();
    
    var formUser = document.querySelector("#formUser");
    console.log(formUser.nome.value);
    console.log(formUser.cpf.value);
    console.log(formUser.data_nasc.value);
    console.log(formUser.endereco.value);
    console.log(formUser.cidade.value);
    console.log(formUser.bairro.value);
    console.log(formUser.cargo_selecionado.value);
    console.log(formUser.gridRadios.value)
    console.log(formUser.email.value);
    console.log(formUser.senha.value);
})