import { createRouter, createWebHistory } from 'vue-router'
import homePage from '../components/homePage.vue'
import registerPage from '../components/registerPage.vue'
import loginPage from '../components/loginPage.vue'
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
  },
  {
    path: '/login',
    name: 'loginPage',
    component: loginPage
  }
  ],
})
console.log('App loaded!')
export default router
