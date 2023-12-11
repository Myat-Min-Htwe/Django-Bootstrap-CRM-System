console.log("hell", 999999);

const ctx = document.getElementById("myChart");

new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      'Sunday',
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday'
    ],
    datasets: [
      {
        data: [
          339,
          345,
          483,
          143,
          489,
          409,
          104
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 3,
        pointBackgroundColor: '#007bff'
      },
    ],
  },
  options: {
    plugins: {
      title: {
        display: true,
        text: 'Dashboard Chart (not set data)'
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
        beginAtZero: true,
      },
    },
  },
});


const sr = ScrollReveal ({
  distance: '80px',
  duration: 2000,
  delay: 450,
  reset: true
});


sr.reveal('.card1',{delay:200, origin: 'top'});
sr.reveal('.card2',{delay:400, origin: 'top'});
sr.reveal('.dashchart',{delay:500, origin: 'bottom'});