import { createRouter, createWebHistory } from 'vue-router'
import homePage from '@/components/homePage.vue'
import newPage from '@/components/newPage.vue'

const routes = [
  {
    path: '/',
    name: 'homePage',
    component: homePage,
  },
  {
    path: '/new',
    name: 'newPage',
    component: newPage,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router


