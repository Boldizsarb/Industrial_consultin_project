<template>
  <Doughnut id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script>
import { Doughnut } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement, // Register ArcElement for the Doughnut chart
  CategoryScale,
  LinearScale,
);

export default {
  name: "DoughnutChart",
  components: { Doughnut },
  data() {
    return {
      chartData: {
        labels: ["Total", "Average"],
        datasets: [
          {
            backgroundColor: [
              "rgba(255, 99, 132, 0.6)",
              "rgba(54, 162, 235, 0.6)",
            ],
            borderColor: ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)"],
            borderWidth: 1,
            data: [90, 30], // The data points for each segment
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
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
  justify-content: center;
  align-items: center;
}
</style>
