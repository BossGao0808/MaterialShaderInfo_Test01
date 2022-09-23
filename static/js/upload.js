function OninputValueChange(chart) {

    $('#number1').on('change', function (event) {

        var number1 = $("input[name='number1']").val();
        chart = new Chart(document.getElementById('chart6'), {
            type: 'doughnut',
            data: {
                labels: ["Mobile", "Desktop", "Tablet"],
                datasets: [{
                    label: "Device Users",
                    backgroundColor: ["#12bf24", "#3461ff", "#ff6632"],
                    data: [number1, 1.2, .03]
                }]
            },
            options: {
                maintainAspectRatio: true,
                cutoutPercentage: 85,
                responsive: true,
                legend: {
                    display: true
                }
            }
        });
    });
}


$(function () {
    "use strict";

    //var vnumber1 = $("input[name='number1']").val();

    var chart = new Chart(document.getElementById('chart6'), {
        type: 'doughnut',
        data: {
            labels: ["Mobile", "Desktop", "Tablet"],
            datasets: [{
                label: "Device Users",
                backgroundColor: ["#12bf24", "#3461ff", "#ff6632"],
                data: [0.5*1000, 1.2*1000, .03*1000]
            }]
        },
        options: {
            maintainAspectRatio: true,
            cutoutPercentage: 85,
            responsive: true,
            legend: {
                display: true
            }
        }
    });

    OninputValueChange(chart);


});