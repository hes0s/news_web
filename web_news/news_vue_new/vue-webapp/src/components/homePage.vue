<template>
  <div class="all">
  <Navbar />
  <div class="text-center mt-2">
    <h1>NewsWeb</h1>
  </div>

  <GridNews />


  
  </div>
</template>

<script>
import Navbar from"@/views/navbar.vue";
import GridNews from "@/views/grid_news.vue";

export default {
  name: 'homePage',
  components: {
    Navbar,
    GridNews // Register the components
  },
};
</script>

<style scoped>
.container {
  background-color: aqua;
}

.Maintext {
  display: flex;
  left: 50%;
}
</style>
