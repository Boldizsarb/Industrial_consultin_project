<template>
  <div class="min-h-screen flex items-center justify-center">
    <div
      class="w-2/3 flex min-h-screen max-w-screen-sm items-center justify-center transition-opacity duration-700 ease-in opacity-0 fade-bottom"
      :class="{ 'opacity-100': isAnimated }"
      @mouseenter="isAnimated = true"
    >
      <div class="relative bg-gray-200 bg-opacity-50 rounded-lg p-4 w-full">
        <router-link to="/" class="absolute top-0 right-0 m-4">
          <img
            src="@/assets/images/back.png"
            alt="Back to Home"
            class="h-8 w-8"
          />
          <!-- Adjust size with h-8 w-8 -->
        </router-link>
        <div>
          <h2
            class="mt-8 text-center text-4xl font-extrabold text-slate-700 tracking-tight"
          >
            Confirm Email
          </h2>
        </div>
        <form class="mt-8 space-y-6" @submit.prevent="requestPasswordReset">
          <div>
            <input
              type="email"
              id="email"
              v-model="email"
              required
              placeholder="Email"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            />
          </div>
          <div v-if="errorMessage" class="text-red-800">
            {{ errorMessage }}
          </div>
          <div v-if="successMessage" class="text-green-800">
            {{ successMessage }}
          </div>
          <div>
            <button
              type="submit"
              class="w-full sm:w-auto bg-slate-700 hover:bg-green-700 flex-1 justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      errorMessage: "",
      successMessage: "",
      isAnimated: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
  },
  methods: {
    requestPasswordReset() {
      this.errorMessage = "";
      this.successMessage = "";
      const requestBody = {
        email: this.email,
      };
      fetch(`${process.env.VUE_APP_BACKEND_URL}/request_password_reset`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
      })
        .then((response) => {
          if (!response.ok) {
            // Handle error case - likely need to parse error from response.json()
            throw new Error("Password reset request failed");
          }
          return response.json();
        })
        .then(() => {
          this.successMessage =
            "If your email is in our system, you will receive a reset link.";
          this.$router.push("/redirect");
        })
        .catch((error) => {
          console.error("Error:", error);
          // Display a user-friendly error message here
          this.errorMessage =
            "An error occurred while sending reset email. Please try again later.";
        });
    },
  },
};
</script>
