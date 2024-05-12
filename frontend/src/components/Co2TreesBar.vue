<!-- components/Co2TreesIconBar.vue -->
<template>
  <div class="w-full p-4">
    <div class="tree-bar-container">
      <div class="tree-bar" :style="{ width: barWidth }">
        <span
          v-for="(n, index) in numberOfTrees"
          :key="index"
          :style="{ color: treeIconColor }"
          class="tree-icon"
        >
          🌲
        </span>
      </div>
    </div>
    <p
      class="mt-4 text-center text-xl font-semibold text-gray-800 dark:text-white"
    >
      <span v-if="numberOfTrees === 0"
        >Keep the good work to save the world !</span
      >
      <span v-if="numberOfTrees > 0"
        >It will take over {{ numberOfTrees }} day/s for an average tree to
        absorve all the co2 emitted!</span
      >
    </p>
  </div>
</template>

<script>
export default {
  props: {
    co2Emission: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      co2totree: 25000,
      treesPer20kg: 1, // Adjust the offset ratio as needed
      healthyThreshold: 100, // Healthy threshold (in kg)
      sickThreshold: 300, // Sick threshold (in kg)
    };
  },
  computed: {
    numberOfTrees() {
      console.log(Math.ceil(this.co2Emission / (this.co2totree / 365)));
      // Calculate the number of trees required based on CO2 emissions
      return Math.ceil(this.co2Emission / (this.co2totree / 365));
    },
    barWidth() {
      // Adjust the bar width proportionally to the number of trees
      const maxTrees = 20; // Example max capacity for the bar
      const percentage = Math.min((this.numberOfTrees / maxTrees) * 100, 100);
      return `${percentage}%`;
    },
    treeIconColor() {
      // Determine the tree icon color based on CO2 emissions
      if (this.co2Emission <= this.healthyThreshold) {
        return "#4caf50"; // Green for healthy
      } else if (this.co2Emission <= this.sickThreshold) {
        return "#ff9800"; // Orange for sick
      } else {
        return "#795548"; // Brown for dead
      }
    },
  },
};
</script>

<style scoped>
.tree-bar-container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  border: 2px solid green;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
  height: 50px;
}

.tree-bar {
  height: 100%;
  display: flex;
  align-items: center;
  transition: width 0.5s ease;
  background-color: transparent;
}

.tree-icon {
  font-size: 24px;
  margin: 0 2px; /* Adjust spacing between tree icons as needed */
}
</style>
