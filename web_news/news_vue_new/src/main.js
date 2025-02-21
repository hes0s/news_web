
import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
const app = createApp(App)
app.use(router)
app.mount('#app')
app.config.devtools = true; // Force enable Vue DevTools
console.log('App loaded!')

