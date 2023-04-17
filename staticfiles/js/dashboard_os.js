google.charts.load("current", {packages:["corechart"]});
  google.charts.setOnLoadCallback(drawChart);
  
  function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Situação', 'Quantidade'],
      ['Finalizadas nos Últimos 30 dias', {{os_FinalizadosRecentes}}],
      ['Concluídas', {{os_Finalizadas}}],
      ['Ativas', {{os_Pendentes}}],
      ['Inativas', {{os_inativas}}],
    ]);

    var options = {
      title: 'ORDENS DE SERVIÇO',
      pieHole: 0.4,
      colors: ['blue', 'green', 'orange', 'red']
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);