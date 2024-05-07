<template>
  <div>
    <h1>Redirecting...</h1>
    <p>Redirecting to login page in {{ countdown }} seconds.</p>
  </div>
</template>

<script>
export default {
  name: "RedirectPage",
  data() {
    return {
      countdown: 5, // Initial countdown value
    };
  },
  mounted() {
    // Start countdown
    this.startCountdown();
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
