<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
);

export default {
  name: "BarChart",
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ["January", "February", "March"],
        datasets: [
          {
            label: "Monthly Carbon Usage",
            backgroundColor: [
              "rgba(255, 99, 132, 0.6)",
              "rgba(54, 162, 235, 0.6)",
              "rgba(255, 206, 86, 0.6)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
            ],
            borderWidth: 1,
            data: [10, 25, 55],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            ticks: {
              color: "#fff", // X-axis ticks color
            },
            grid: {
              color: "rgba(255, 255, 255, 0.1)", // X-axis grid lines color
            },
          },
          y: {
            ticks: {
              color: "#fff", // Y-axis ticks color
            },
            grid: {
              color: "rgba(255, 255, 255, 0.1)", // Y-axis grid lines color
            },
          },
        },
        plugins: {
          legend: {
            labels: {
              color: "#fff", // Make legend text color white
            },
          },
          tooltip: {
            titleFontColor: "#fff", // Title color
            bodyFontColor: "#fff", // Body color
            footerFontColor: "#fff", // Footer color
            backgroundColor: "rgba(0, 0, 0, 0.7)", // Tooltip background color
          },
        },
      },
    };
  },
};
</script>

<style scoped>
div {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
