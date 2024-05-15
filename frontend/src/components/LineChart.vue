<template>
  <div class="chart-container">
    <Bar ref="myChart" :options="chartOptions" :data="chartData" />
  </div>
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
  props: {
    monthValues: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      chartData: {
        labels: [], // These will be populated dynamically
        datasets: [
          {
            label: "Co2",
            backgroundColor: [
              "rgba(255, 99, 132, 0.6)",
              "rgba(54, 162, 235, 0.6)",
              "rgba(255, 206, 86, 0.6)",
              "rgba(75, 192, 192, 0.6)",
              "rgba(153, 102, 255, 0.6)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
            ],
            borderWidth: 1,
            data: [], // These will be populated dynamically
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
  watch: {
    monthValues: {
      immediate: true,
      handler(newData) {
        this.updateChartData(newData);
      },
    },
  },
  methods: {
    updateChartData(data) {
      if (!data) return; // Check for null or undefined data

      // Ensure valid entries and remove undefined/null values
      const validEntries = Object.entries(data).filter(
        ([key, value]) => key && value !== null && value !== undefined,
      );

      // Extract labels and data based on provided months and values
      const labels = validEntries.map(([key]) => key);
      const values = validEntries.map(([, value]) => value);

      // Update the labels and data for the chart
      this.chartData.labels = labels;
      this.chartData.datasets[0].data = values;

      // Trigger chart update
      if (this.$refs.myChart) {
        this.$refs.myChart.update();
      }
    },
  },
};
</script>

<style scoped>
.chart-container {
  height: 50vh; /* Fixed to 50% of the viewport height */
  width: 100%;
  display: flex;
}
</style>
