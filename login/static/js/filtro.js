$(document). ready(function(){

var baseUrl = 'http://localhost:8000/';
var filtro = $('#filtro');

    $(filtro).change(function(){

        var filtro = $(this).val();
        window.location.href = baseUrl + '?filtro=' + filtro;

    })

});