<template>
  <navbar />
  <div class="min-h-screen flex justify-center items-center">
    <div
      class="overflow-y-scroll scrollbar-thin scrollbar-thumb-gray-500 scrollbar-track-gray-200 w-full h-full max-h-[60vh] max-w-[80vw] bg-gray-200 bg-opacity-50 rounded-lg shadow-lg transition-opacity duration-700 ease-in opacity-0"
      :class="{ 'opacity-100': isAnimated }"
    >
      <info />
    </div>
  </div>
  <myFooter />
</template>

<script>
import navbar from "@/components/MainPageNav.vue";
import myFooter from "@/components/Footer.vue";
import info from "@/components/MainPageInfo.vue";

export default {
  name: "HomePage",
  components: {
    navbar,
    myFooter,
    info,
  },
  data() {
    return {
      isAnimated: false,
      heroStats: [
        { title: "Global Average Emissions", value: "36.8 Billion Tons" },
        { title: "Annual Increase", value: "2.5%" },
        { title: "Impact on Temperature", value: "+1.5°C" },
      ],
      infoCards: [
        {
          title: "Impact on Health",
          description:
            "Rising emissions lead to more smog and respiratory problems, particularly affecting urban areas.",
        },
        {
          title: "Ocean Acidification",
          description:
            "Increased CO2 levels are altering ocean chemistry, impacting marine life and food chains.",
        },
        {
          title: "Solutions and Reductions",
          description:
            "Explore actionable ways to reduce emissions through renewable energy and lifestyle changes.",
        },
      ],
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
