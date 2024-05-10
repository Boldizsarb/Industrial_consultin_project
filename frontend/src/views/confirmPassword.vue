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
            Set New Password
          </h2>
        </div>
        <form class="mt-8 space-y-6" @submit.prevent="confirmPasswordReset">
          <div>
            <input
              type="password"
              id="password"
              v-model="password"
              :class="{ 'border-red-800': passwordError }"
              @input="checkPasswords"
              required
              placeholder="New Password"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            />
          </div>
          <div>
            <input
              type="password"
              id="confirmPassword"
              v-model="confirmPassword"
              :class="{ 'border-red-800': passwordError }"
              @input="checkPasswords"
              required
              placeholder="Confirm New Password"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            />
          </div>
          <span
            :class="{
              hidden: !passwordError,
              'text-red-800': passwordError,
            }"
          >
            Passwords Don't Match
          </span>
          <div>
            <button
              type="submit"
              class="w-full sm:w-auto bg-slate-700 hover:bg-green-700 flex-1 justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Reset Password
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
      password: "",
      confirmPassword: "",
      resetToken: "",
      email: "",
      passwordError: false,
      isAnimated: false,
    };
  },
  mounted() {
    // Extract the reset token and email from the URL
    this.resetToken = this.$route.params.token;
    this.email = this.$route.query.email;
    console.log(this.email);
    console.log(this.resetToken);
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
  },
  methods: {
    checkPasswords() {
      if (this.password !== this.confirmPassword) {
        this.passwordError = true;
      } else {
        this.passwordError = false;
      }
    },
    confirmPasswordReset() {
      if (this.passwordsMatch) {
        alert("Passwords do not match");
        return;
      }

      // Call the backend endpoint to coinfirm the password reset
      fetch(`${process.env.VUE_APP_BACKEND_URL}/confirm_password_reset`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: this.email,
          resetToken: this.resetToken,
          password: this.password,
        }),
      })
        .then(async (response) => {
          const data = await response.json();
          if (response.ok) {
            alert("Password reset successful");
            this.$router.push("/login");
          } else {
            console.error("Error from the backend", data);
            alert(
              data.message || "An error occurred while processing your request",
            );
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("An error occurred while processing your request");
        });
    },
  },
};
</script>
