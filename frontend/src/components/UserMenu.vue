<template>
  <div class="relative" ref="menuContainer">
    <button
      @click="toggleMenu"
      class="flex items-center focus:outline-none mr-3"
    >
      <slot name="button"></slot>
    </button>
    <div
      v-if="menuVisible"
      class="absolute bg-gray-900 rounded shadow-md mt-2 min-w-full overflow-auto z-30"
    >
      <ul class="list-reset">
        <li>
          <router-link
            to="/userDetails"
            class="px-4 py-2 block text-gray-100 hover:bg-gray-800 no-underline hover:no-underline"
          >
            My Details
          </router-link>
        </li>
        <li>
          <hr class="border-t mx-2 border-gray-400" />
        </li>
        <li>
          <button
            @click="logout"
            class="px-4 py-2 block text-gray-100 hover:bg-gray-800 no-underline hover:no-underline"
          >
            Logout
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menuVisible: false,
    };
  },
  methods: {
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    getCookie(name) {
      let cookieArray = document.cookie.split(";");
      for (let i = 0; i < cookieArray.length; i++) {
        let cookiePair = cookieArray[i].split("=");
        if (name === cookiePair[0].trim()) {
          return decodeURIComponent(cookiePair[1]);
        }
      }
      return null;
    },
    logout() {
      const token = this.getCookie("token");
      if (!token) {
        console.error("No token found.");
        this.$router.push("/login");
        return;
      }
      fetch(`${process.env.VUE_APP_BACKEND_URL}/logout`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
        .then((response) => {
          console.log("Logout response received"); // Debugging log
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          this.$router.push("/login");
          console.log("Logout successful:", data); // Debugging log
        })
        .catch((error) => {
          console.error("Error during logout:", error);
          this.$router.push("/login");
        });
    },
    handleClickOutside(event) {
      if (
        this.$refs.menuContainer &&
        !this.$refs.menuContainer.contains(event.target)
      ) {
        this.menuVisible = false;
      }
    },
  },

  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside);
  },
};
</script>
