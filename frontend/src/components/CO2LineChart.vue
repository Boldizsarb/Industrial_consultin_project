<!-- CO2LineChart.vue -->
<template>
  <div class="chart-container">
    <line-chart :data="chartData" :options="chartOptions"></line-chart>
  </div>
</template>

<script>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from "chart.js";

// Register Chart.js components
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
);

export default {
  name: "CO2LineChart",
  components: {
    "line-chart": Line,
  },
  data() {
    return {
      chartData: {
        labels: [
          "2000",
          "2001",
          "2002",
          "2003",
          "2004",
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
          "2021",
          "2022",
          "2023",
        ],
        datasets: [
          {
            label: "CO2 Emissions (Billion Metric Tons)",
            data: [
              25.5, 25.67, 26.25, 27.65, 28.62, 29.59, 30.61, 31.5, 32.04,
              31.49, 33.31, 34.44, 34.94, 35.23, 35.47, 35.46, 35.46, 36.03,
              36.77, 37.04, 35.01, 36.82, 37.15, 37.55,
            ],
            backgroundColor: "rgba(255, 0, 0, 1)",
            borderColor: "rgba(255, 0, 0, 1)", // Solid yellow
            borderWidth: 2,
            fill: true,
            tension: 0.2,
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "top",
            labels: {
              color: "#333", // Adjust to desired label color
            },
          },
          tooltip: {
            enabled: true,
            mode: "index",
            intersect: false,
          },
        },
        scales: {
          x: {
            ticks: {
              color: "#333",
            },
            grid: {
              color: "rgba(0, 0, 0, 0.1)",
            },
          },
          y: {
            ticks: {
              color: "#333",
            },
            grid: {
              color: "rgba(0, 0, 0, 0.1)",
            },
            title: {
              display: true,
              text: "Billion Metric Tons",
              color: "#333",
            },
          },
        },
      },
    };
  },
};
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 400px; /* Adjust height as needed */
}
</style>
