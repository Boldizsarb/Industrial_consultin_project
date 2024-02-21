<template>
  <div class="min-h-screen flex justify-center items-center">
    <div
      class="w-3/4 bg-gray-200 bg-opacity-50 rounded-lg shadow-lg p-4 transition-opacity duration-700 ease-in opacity-0"
      :class="{ 'opacity-100': isAnimated }"
    >
      <h1 class="text-4xl font-bold mb-4 text-slate-700">
        Measure Your Carbon Footprint
      </h1>
      <p class="text-lg mb-6 text-slate-700">
        Join us in our effort to make the earth a greener place. Start by
        understanding your carbon footprint.
      </p>
      <div class="space-x-4 mt-6">
        <router-link
          to="/login"
          class="bg-slate-700 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
          >Sign in</router-link
        >
        <router-link
          to="/signup"
          class="bg-slate-700 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
          >Create Account</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      isAnimated: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.isAnimated = true;
    }, 100); // Start the animation shortly after the component mounts
  },
};
</script>

<style scoped>
/* Additional styles if needed */
</style>
