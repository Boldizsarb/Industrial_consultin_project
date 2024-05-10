<template>
  <navbar />
  <div class="min-h-screen flex justify-center items-center p-4">
    <div
      class="w-full max-w-4xl bg-gray-500 bg-opacity-50 rounded-lg shadow-lg transition-opacity duration-700 ease-in relative p-6"
      :class="{ 'opacity-100': isAnimated }"
    >
      <div class="text-white">
        <h1 class="text-3xl font-bold text-white mb-2">Monthly Carbon Usage</h1>
        <BarChart :monthValues="monthValues" />
      </div>
    </div>
  </div>
  <myFooter />
</template>

<script>
import BarChart from "@/components/LineChart.vue";
import navbar from "@/components/NavBar.vue";
import myFooter from "@/components/Footer.vue";

export default {
  name: "DashBoard",
  components: {
    BarChart,
    navbar,
    myFooter,
  },
  data() {
    return {
      isAnimated: false,
      user_id: null,
      monthValues: {
        January: 10,
        February: 25,
        March: 55,
        April: 40,
        May: 30,
        June: 55,
        Jully: 40,
        August: 30,
      },
    };
  },
  methods: {
    getCo2Emmissions() {
      fetch(`${process.env.VUE_APP_BACKEND_URL}/userTotalEmissions`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: this.user_id,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (data.message) {
            alert(data.message); // This will show the message from your Flask API as an alert
          }
          this.monthValues = data.month_values;
        })
        .catch((error) => {
          console.error("There was a problem adding the trip:", error);
        });
    },
  },
  mounted() {
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
  },
};
</script>
