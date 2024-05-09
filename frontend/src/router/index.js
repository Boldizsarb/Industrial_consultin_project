import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Main",
    component: () => import("../views/MainPage.vue"),
    meta: { hideMenu: true, requiresAuth: false, guestOnly: true },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
    meta: { hideMenu: true, requiresAuth: false, guestOnly: true },
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("../views/Signup.vue"),
    meta: { hideMenu: true, requiresAuth: false, guestOnly: true },
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
  const guestOnly = to.matched.some((record) => record.meta.guestOnly);
  const token = getCookie("token");
  console.log("Token:", token);

  if (requiresAuth) {
    // Send a request to the backend to verify the token
    fetch("http://localhost:5000/verify-token", {
      method: "POST",
      headers: {
        Authorization: token,
      },
      body: JSON.stringify({ token }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Data:", data);
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
  } else if (guestOnly && token) {
    // User is authenticated and trying to access a guest-only route, redirect to the dashboard
    next("/dashboard");
  } else {
    // Route doesn't require authentication or is a guest-only route, allow access
    next();
  }
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

export default router;
