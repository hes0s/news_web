<template>
  <div class="all">
    <!-- Highlight the Latest News -->
    <div v-if="items.length > 0" class="card mb-3 mx-auto mt-5" style="width: 800px; height: 500px">
      <img :src="items[0].photo" class="card-img-top" alt="Latest News Photo" />
      <div class="card-body">
        <h4 class="card-sub-title">Noutatea zilei</h4>
        <h5 class="card-title">{{ items[0].name }}</h5>
        <p class="card-text">{{ items[0].description }}</p>
        <p class="card-text"><small class="text-body-secondary">Last updated just now</small></p>
      </div>
    </div>

    <!-- Grid of Other News -->
    <div class="row row-cols-1 row-cols-md-3 g-4 mx-auto" style="width: 800px">
      <div v-for="(news, index) in items.slice(1)" :key="index" class="col">
        <div class="card h-100">
          <img :src="news.photo" class="card-img-top" alt="News Photo" />
          <div class="card-body">
            <h5 class="card-title">{{ news.name }}</h5>
            <p class="card-text">{{ news.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  name: "GridNews",
  
  data() {
    return {
      newsList: [],
    };
  },

  methods: {
    async fetchNews() {
      const response = await axios.get("http://localhost:3000/news");
      this.newsList = response.data;
    },
  },

  mounted() {
    this.fetchNews();
  },
};
</script>

<style>
.card {
  border-radius: 10px;
  overflow: hidden;
}

.card img {
  object-fit: cover;
  height: 200px;
}

.card-body {
  text-align: center;
}
</style>