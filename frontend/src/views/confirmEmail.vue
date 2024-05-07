<template>
  <div>
    <h1>Reset Password</h1>
    <form @submit.prevent="requestPasswordReset">
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>
    <div v-if="successMessage" class="success-message">
      {{ successMessage }}
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
    };
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
