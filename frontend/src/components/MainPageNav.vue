<template>
  <nav id="header" class="bg-gray-900 fixed w-full z-10 top-0 shadow">
    <div
      class="w-full container mx-auto flex flex-wrap items-center mt-0 pt-3 pb-3 md:pb-0"
    >
      <div class="w-1/2 pl-2 md:pl-0">
        <router-link
          to="/"
          class="flex items-center space-x-3 rtl:space-x-reverse"
        >
          <img
            src="@/assets/images/logo.png"
            class="h-8 rounded-full"
            alt="Flowbite Logo"
          />
          <span
            class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white"
            >CO2 Emissions</span
          >
        </router-link>
      </div>
      <div class="w-1/2 pr-0">
        <div class="flex relative inline-block float-right">
          <div class="block md:hidden pr-4">
            <button
              @click="toggleMenu"
              id="nav-toggle"
              class="flex items-center px-3 py-2 border rounded text-gray-500 border-gray-600 hover:text-gray-100 hover:border-teal-500 appearance-none focus:outline-none"
            >
              <svg
                class="fill-current h-3 w-3"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <title>Menu</title>
                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div
        :class="[
          !isMenuOpen ? 'hidden' : 'flex',
          'w-full',
          'flex-grow',
          'md:flex',
          'md:items-center',
          'md:w-auto',
          'md:block',
          'mt-2',
          'md:mt-0',
          'bg-gray-900',
          'z-20',
        ]"
        id="navbar-sticky"
      >
        <ul
          class="flex flex-col w-full p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
        >
          <li class="mr-6 my-2 md:my-0">
            <router-link
              to="/login"
              class="block py-1 md:py-3 pl-1 align-middle text-gray-500 no-underline hover:text-gray-100 border-b-2 border-gray-900 hover:border-yellow-400"
              active-class="text-white"
              aria-current="page"
            >
              <i class="fas fa-user fa-fw"></i>
              <span class="pb-1 md:pb-0 text-sm">Sign In</span>
            </router-link>
          </li>
          <li class="mr-6 my-2 md:my-0">
            <router-link
              to="/signup"
              class="block py-1 md:py-3 pl-1 align-middle text-gray-500 no-underline hover:text-gray-100 border-b-2 border-gray-900 hover:border-red-400"
              active-class="text-white "
              aria-current="page"
            >
              <i class="fas fa-user-plus fa-fw"></i>
              <span class="pb-1 md:pb-0 text-sm">Sing Up</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",

  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
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
