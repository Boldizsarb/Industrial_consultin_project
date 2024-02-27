<template>
  <nav
    class="top-0 left-0 right-0 shadow-md p-6 bg-gray-500 bg-opacity-100 rounded-b-lg"
  >
    <ul class="flex justify-center space-x-4">
      <li>
        <router-link to="/dashboard" v-slot="{ isActive }">
          <a
            :class="[
              'text-blue-300 hover:text-blue-500 font-semibold',
              isActive ? 'text-blue-700' : '',
            ]"
            >Dashboard</a
          >
        </router-link>
      </li>
      <li>
        <router-link to="/about" v-slot="{ isActive }">
          <a
            :class="[
              'text-blue-300 hover:text-blue-500 font-semibold',
              isActive ? 'text-blue-700' : '',
            ]"
            >About</a
          >
        </router-link>
      </li>
      <li>
        <router-link to="/contact" v-slot="{ isActive }">
          <a
            :class="[
              'text-blue-300 hover:text-blue-500 font-semibold',
              isActive ? 'text-blue-700' : '',
            ]"
            >Contact</a
          >
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
/* Custom animation for sliding down */
@keyframes slideDown {
  from {
    transform: translateY(-100%);
  }
  to {
    transform: translateY(0);
  }
}
nav {
  animation: slideDown 0.5s ease-out forwards;
}
</style>
