<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
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
  background-attachment: fixed; /* Ensures the background is static */
  background-size: cover; /* Scales the image while maintaining aspect ratio */
  background-repeat: no-repeat; /* Prevents tiling of the image */
  background-position: center; /* Centers the image within the viewport */
  min-height: 100vh; /* Make sure the div takes at least the full viewport height */
}
</style>
