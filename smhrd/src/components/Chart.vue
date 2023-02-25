<template>
  <Line :data="chartData" :options="chartOptions"/>
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineController, PointElement, LineElement, LinearScale, CategoryScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineController, PointElement, LineElement, LinearScale, CategoryScale)

export default {
  name: 'LineChart',
  components: { Line },
  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March'],
        datasets: [
          {
            label: 'Sepsis Score',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            borderWidth: 1,
            data: [0, 10, 5, 2, 20, 30, 45],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        scales: {
          x: {
            type: 'category', // x축의 스케일을 category로 설정합니다.
            labels: ['A', 'B', 'C'], // x축 레이블을 설정합니다.
          },
          y: {
            beginAtZero: true,
          },
        },
      },
    };
  },
};
</script>
