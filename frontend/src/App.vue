<template>
  <div id="app">
    <navbar v-if="!$route.meta.hideMenu" />
    <router-view />
  </div>
</template>

<script>
import navbar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    navbar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url("@/assets/images/home-page.jpg");
  background-size: cover;
  background-position: center center;
  min-height: 100vh; /* Make sure the div takes at least the full viewport height */
}
</style>
