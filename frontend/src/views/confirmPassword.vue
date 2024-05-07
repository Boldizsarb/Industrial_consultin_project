<template>
  <div>
    <h1>Set New Password</h1>
    <form @submit.prevent="confirmPasswordReset">
      <div>
        <label for="password">New Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <label for="confirmPassword">Confirm New Password</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          required
        />
      </div>
      <div>
        <button type="submit" :disabled="!passwordsMatch">
          Reset Password
        </button>
        <span v-if="!passwordsMatch">Passwords do not match</span>
      </div>
    </form>
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
    };
  },
  mounted() {
    // Extract the reset token and email from the URL
    this.resetToken = this.$route.params.token;
    this.email = this.$route.query.email;
    console.log(this.email);
    console.log(this.resetToken);
  },
  computed: {
    passwordsMatch() {
      return this.password && this.password === this.confirmPassword;
    },
  },
  methods: {
    confirmPasswordReset() {
      if (!this.passwordsMatch) {
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
