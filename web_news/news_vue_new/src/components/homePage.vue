<script>
import navbar from"@/views/navbar.vue"
import GridNews from "@/views/grid_news.vue";

export default {
  components: {
    navbar,
    GridNews,
  },
  name: 'homePage',
};
</script>
<template>
  <div class="all">
  <navbar />
  <div class="text-center mt-2">
    <h1>NewsWeb</h1>
  </div>

  <GridNews />

  </div>
</template>



<style scoped>
.container {
  background-color: aqua;
}

.Maintext {
  display: flex;
  left: 50%;
}
</style>
