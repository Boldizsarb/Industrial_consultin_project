<template>
  <div class="min-h-screen flex justify-center items-center p-4">
    <div
      class="w-full max-w-4xl bg-gray-500 bg-opacity-50 rounded-lg shadow-lg transition-opacity duration-700 ease-in relative p-6"
      :class="{ 'opacity-100': isAnimated }"
    >
      <!-- Adjusted Button Container -->
      <div class="w-full md:w-auto">
        <button
          @click="toggleInput"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-full md:w-auto"
        >
          Add Trip
        </button>
      </div>

      <div class="text-white">
        <h1>Welcome user abcd</h1>
        <p>This is your carbon emission summary</p>
        <select
          v-model="chartType"
          class="text-black bg-white border border-gray-300 p-2 rounded-md"
        >
          <option value="bar">Bar Chart</option>
          <option value="doughnut">Doughnut Chart</option>
        </select>
        <div v-if="chartType === 'bar'" class="w-full">
          <BarChart />
        </div>
        <div v-if="chartType === 'doughnut'" class="w-full">
          <DoughnutChart />
        </div>
      </div>
    </div>
  </div>

  <transition name="fade">
    <div
      v-if="showInput"
      class="fixed inset-0 bg-gray-500 bg-opacity-75 flex justify-center items-center"
    >
      <div class="bg-white p-4 rounded-lg max-w-md w-full space-y-4">
        <div class="text-lg font-semibold">Add new trip</div>
        <select
          v-model="type"
          class="bg-gray-200 text-gray-700 py-1 px-2 rounded"
        >
          <option disabled value="">Select a mean of transport</option>
          <option
            v-for="typeItem in typeList"
            :key="typeItem.value"
            :value="typeItem.value"
          >
            {{ typeItem.name }}
          </option>
        </select>
        <input
          v-if="type === 'car'"
          v-model="reg"
          placeholder="Registration Plate"
          class="bg-gray-200 text-gray-700 py-1 px-2 rounded"
        />
        <input
          v-model="distance"
          type="number"
          placeholder="Distance of travel"
          class="bg-gray-200 text-gray-700 py-1 px-2 rounded"
        />

        <div class="flex justify-center space-x-2">
          <button
            @click="addTrip()"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Save
          </button>
          <button
            @click="
              showInput = false;
              reg = '';
              distance = '';
              type = '';
            "
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import BarChart from "@/components/LineChart.vue";
import DoughnutChart from "@/components/DoughnutChart.vue";

export default {
  name: "DashBoard",
  components: {
    BarChart,
    DoughnutChart,
  },
  data() {
    return {
      isAnimated: false,
      showInput: false,
      chartType: "bar",
      typeList: [
        { value: "car", name: "Car" },
        { value: "bus", name: "Bus" },
        { value: "train", name: "Train" },
        { value: "plain", name: "Plain" },
      ],
      type: "",
      reg: "",
      distance: "",
    };
  },
  methods: {
    toggleInput() {
      this.showInput = !this.showInput;
      // Initialize data here if needed
      if (this.showInput) {
        // Reset the input field when opening the modal
        this.type = "";
        this.reg = "";
        this.distance = "";
      }
    },
    addTrip() {
      const regIn = this.reg.trim();
      const distanceIn = this.distance;
      const typeIn = this.type.trim();
      if (!regIn && typeIn === "car") {
        alert("Your registration nubmer is required");
        return;
      } else if (!distanceIn && distanceIn <= 0) {
        alert("You need to enter a valid distance");
        return;
      } else if (!typeIn) {
        alert("You need to chose a valid type");
        return;
      }
      console.log(regIn, distanceIn, typeIn);
      fetch(`${process.env.VUE_APP_BACKEND_URL}/calculate_emission`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          reg: regIn,
          miles: distanceIn,
          type: typeIn,
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
          this.showInput = false;
          this.reg = "";
          this.distance = "";
          this.type = "";
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
