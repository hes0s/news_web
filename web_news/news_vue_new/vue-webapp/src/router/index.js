import { createRouter, createWebHistory } from 'vue-router'
import homePage from '../components/homePage.vue'
import registerPage from '../components/registerPage.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
    path: '/',
    name: 'Home',
    component: homePage
  },
  {
    path: '/register',
    name: 'registerPage',
    component: registerPage
  }
  ],
})

export default router
