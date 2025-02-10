import { createRouter, createHashHistory } from 'vue-router'
import homePage from '../components/homePage.vue'
import registerPage from '../components/registerPage.vue'
import registerPage from '../components/loginPage.vue'
const router = createRouter({
  history: createHashHistory(import.meta.env.BASE_URL),
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

export default router
