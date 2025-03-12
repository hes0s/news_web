<template>
  <div class="all">
    <!-- Highlight the Latest News -->
    <div class="card mb-3 mx-auto mt-5" style="width: 800px; height: 500px">
      <img src="./aboba.jpg" class="card-img-top" alt="Latest News Photo" />
      <div class="card-body">
        <h4 class="card-sub-title">Noutatea zilei</h4>
        <h5 class="card-title"></h5>
        <p class="card-text"></p>
        <p class="card-text"><small class="text-body-secondary">Last updated just now</small></p>
      </div>
    </div>

    <!-- Grid of Other News -->
    <div class="row row-cols-1 row-cols-md-3 g-4 mx-auto" style="width: 800px">
      <div class="col" v-for="news in newsList" :key="news.id">
        <div class="card h-100">
          <img id="imgContainer" v-if="news.IMG_URL" :src="news.photo" alt="News Image">
          <div class="card-body">
            <h5 class="card-title">{{ news.newsName }}</h5>
            <p class="card-text">{{ news.newsDesription }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue';

export default {
  name: "GridNews",
  setup() {
    const newsList = ref([]); 
    const fetchNews = async () => {
      try {
        const response = await fetch("http://localhost:3000/news"); 
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const data = await response.json();
        console.log("Fetched News Data:", data);
        newsList.value = data;
      } catch (error) {
        console.error("Error fetching news:", error);
      }
    };
    onMounted(fetchNews); 

    return { newsList };
  }
};

const imgContainer = document.getElementById("imgContainer");
const nrImg = 5;

for(let i; i <= 1; i++){
  
}
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