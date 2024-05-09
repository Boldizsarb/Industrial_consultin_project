import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Main",
    component: () => import("../views/MainPage.vue"),
    meta: { hideMenu: true, requiresAuth: false },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
    meta: { hideMenu: true, requiresAuth: false },
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("../views/Signup.vue"),
    meta: { hideMenu: true, requiresAuth: false },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("../views/Dashboard.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/contact",
    name: "Contact",
    component: () => import("../views/Contact.vue"),
    meta: { requiresAuth: true },
  },
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  const token = getCookie("token");

  if (requiresAuth) {
    // Send a request to the backend to verify the token
    fetch("http://localhost:5000/verify-token", {
      method: "POST",
      headers: {
        Authorization: token,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "valid") {
          // Token is valid, allow access to the route
          next();
        } else {
          // Token is invalid or expired, redirect to the login page
          next("/login");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        // Handle any errors that occurred during the token verification
        next("/login");
      });
  } else {
    // Route doesn't require authentication, allow access
    next();
  }
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

export default router;