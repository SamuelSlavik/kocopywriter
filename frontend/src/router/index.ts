import { createRouter, createWebHistory } from 'vue-router'
import Homepage from "@/pages/sections/Homepage.vue";
import OnePage from "@/pages/OnePage.vue";

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
      path: '/about',
      name: 'about',
      component: Homepage
    }
  ]
})

export default router
