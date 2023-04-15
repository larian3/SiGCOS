const form = document.getElementById("formCF");;
const cnpj = document.getElementById("cnpj");
const razaoSocial = document.getElementById("razaoSocial");
const nomeFant = document.getElementById("nomeFant");
const rg = document.getElementById("rg");
const numero = document.getElementById("numero");
const email = document.getElementById("email");
const complemento = document.getElementById("complemento");
const pais = document.getElementById("pais");
const situacao = document.getElementById("situacao");

var btnAdc = document.querySelector("#btnAdc");

//Botão Adicionar;
btnAdc.addEventListener("click", function(event){
    //Evita o carregamento da página;
    event.preventDefault();
    
    var formCF = document.querySelector("#formCF");
    console.log(formCF.cnpj.value);
    console.log(formCF.razaoSocial.value);
    console.log(formCF.nomeFant.value);
    console.log(formCF.rg.value);
    console.log(formCF.numero.value);
    console.log(formCF.email.value);
    console.log(formCF.complemento.value)
    console.log(formCF.pais.value);
    console.log(formCF.situacao.value);
});