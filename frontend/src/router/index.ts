import { createRouter, createWebHistory } from 'vue-router'
import Homepage from "@/pages/sections/Homepage.vue";
import OnePage from "@/pages/OnePage.vue";
import Login from "@/pages/admin/Login.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: OnePage
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})

export default router
