<template>
  <footer
    class="fixed bottom-0 left-0 z-20 w-full p-4 bg-white border-t border-gray-200 shadow md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600"
  >
    <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400"
      >© 2024 Data Mango. All Rights Reserved.
    </span>
  </footer>
</template>

<script>
export default {
  name: "FooterPage",
};
</script>

<style scoped>
/* Custom animation for sliding down */
@keyframes slideUp {
  from {
    transform: translateY(+100%);
  }
  to {
    transform: translateY(0);
  }
}
footer {
  animation: slideUp 0.5s ease-out forwards;
}
</style>
