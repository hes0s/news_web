<template>
  <Navbar />
  <grid_news />
</template>

<script>
import Navbar from '../views/navbar.vue'
import grid_news from '../views/grid_news.vue'

export default {
  name: 'homePage',
  components: {
    Navbar,
    grid_news, // Register the components
  },
}
</script>

<style scoped>
.container {
  background-color: aqua;
}
</style>
