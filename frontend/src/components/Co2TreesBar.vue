<template>
  <div class="w-full p-4">
    <div class="tree-bar-container">
      <div class="tree-bar" :style="barStyle"></div>
    </div>
    <div class="mt-4 text-center text-xl font-semibold text-black">
      <span v-if="daysToAbsorbCO2 === 0"
        >That trip does not emit any CO2. Keep up the good work to save the
        world!</span
      >
      <span v-if="daysToAbsorbCO2 > 0"
        >It will take over {{ daysToAbsorbCO2 }} day/s for an average tree to
        absorb all the CO2 emitted!</span
      >
    </div>
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
      co2totree: 25000, // CO2 absorption rate in grams
    };
  },
  computed: {
    daysToAbsorbCO2() {
      return Math.ceil(this.co2Emission / (this.co2totree / 365));
    },
    barStyle() {
      const percentage = (this.daysToAbsorbCO2 / 365) * 100;
      return {
        width: `${percentage}%`,
      };
    },
  },
};
</script>

<style scoped>
.tree-bar-container {
  width: 100%;
  max-width: 600px;
  height: 20px;
  background: rgba(76, 175, 80, 0);
  border-radius: 10px;
  overflow: hidden;
}

.tree-bar {
  height: 100%;
  border-radius: 10px;
  background: linear-gradient(to right, #4caf50 0%, #ff9800 50%, #8b4513 100%);
  transition: width 0.5s ease;
}
</style>
