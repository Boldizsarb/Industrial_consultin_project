<template>
  <div class="min-h-screen flex items-center justify-center">
    <div
      class="w-2/3 flex min-h-screen max-w-screen-sm items-center justify-center transition-opacity duration-700 ease-in opacity-0 fade-bottom"
      :class="{ 'opacity-100': isAnimated }"
      @mouseenter="isAnimated = true"
    >
      <div class="relative bg-gray-200 bg-opacity-50 rounded-lg p-4 w-full">
        <h1>Redirecting...</h1>
        <p>Redirecting to login page in {{ countdown }} seconds.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RedirectPage",
  data() {
    return {
      countdown: 5,
      isAnimated: false,
    };
  },
  mounted() {
    // Start countdown
    this.startCountdown();
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
  },
  methods: {
    startCountdown() {
      // Decrement countdown every second
      const timer = setInterval(() => {
        this.countdown--;
        if (this.countdown === 0) {
          // Navigate to login page when countdown reaches 0
          clearInterval(timer); // Stop the timer
          this.$router.push("/login");
        }
      }, 1000); // Run every second (1000 milliseconds)
    },
  },
};
</script>
