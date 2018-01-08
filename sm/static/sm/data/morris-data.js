$(function() {
    function update_donut_chart(){
        $.ajax({
            url: 'http://localhost:8000/api/tendencias/?format=json',
            type: 'GET',
            dataType: 'json',
        })
        .done(function(data) {
            // Cambiamos las key 'nom_tendencia' y 'total_ocurrencias'
            data.forEach(function(element){
                element.label = element.nom_tendencia;
                delete element.nom_tendencia;

                element.value = element.total_ocurrencias;
                delete element.total_ocurrencias;
            });

            $("#morris-donut-chart").empty();
            Morris.Donut({
                element: 'morris-donut-chart',
                data: data,
                resize: true
            });
        })
        .fail(function() {
            console.log("No se ha podido obtener tendencias.");
        })
    }
    $("#update-donut-chart").on("click", update_donut_chart);
});
