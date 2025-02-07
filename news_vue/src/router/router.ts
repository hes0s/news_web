import { createRouter, createWebHistor, RouteRecordRaw } from 'vue-router'
import homePage from '@/components/home/homePage.vue'
import registerPage from '@/components/registration/registerPage.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'homePage',
    component: homePage,
  },
  {
    path: '/register',
    name: 'registerPage',
    component: registerPage,
  },
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
export default router
