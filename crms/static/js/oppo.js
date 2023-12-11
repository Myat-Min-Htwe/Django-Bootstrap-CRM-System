console.log('hellooooooooooo')
document.addEventListener('DOMContentLoaded', function() {

    const ctx = document.getElementById('myChart');

    function updateChart(labels, dataValues) {
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Customers',
                    data: dataValues,
                    lineTension: 0,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.1)',
                        'rgba(127, 0, 255, 0.1)',
                        'rgba(255, 159, 64, 0.1)',
                        'rgba(255, 205, 86, 0.1)',
                        'rgba(75, 192, 192, 0.1)',
                        'rgba(54, 162, 235, 0.1)',
                        'rgba(153, 102, 255, 0.1)',
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(201, 203, 207)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                    ],
                    borderWidth: 1,
                    pointBackgroundColor: '#007bff'
                }]
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Last 7 days Customers'
                    },
                    legend: {
                        display: false
                    },
                    tooltip: {
                        boxPadding: 3
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    fetch('/get_customer_count_data/')
    .then(response => response.json())
    .then(data => {
        const labels = data.labels;
        const dataValues = data.dataValues;

        updateChart(labels, dataValues);
    })
    .catch(error => console.error('Error fetching customer data:', error))
});