<template>
  <div class="all">
    <!-- Highlighted News (Latest News) -->
    <div v-if="latestNews" class="card mb-3 mx-auto mt-5" style="width: 800px; height: 500px">
      <img :src="latestNews.photo" class="card-img-top" alt="News Image" />
      <div class="card-body">
        <h4 class="card-sub-title">Noutatea zilei</h4>
        <h5 class="card-title">{{ latestNews.name }}</h5>
        <p class="card-text">{{ latestNews.description }}</p>
        <p class="card-text"><small class="text-body-secondary">Last updated just now</small></p>
      </div>
    </div>

    <!-- News Grid -->
    <div class="row row-cols-1 row-cols-md-3 g-4 mx-auto" style="width: 800px">
      <div v-for="article in newsList" :key="article._id" class="col">
        <div class="card h-100">
          <img :src="article.photo" class="card-img-top" alt="News Image" />
          <div class="card-body">
            <h5 class="card-title">{{ article.name }}</h5>
            <p class="card-text">{{ article.description }}</p>
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
  setup() {
    const newsList = ref([]); // All news articles
    const latestNews = ref(null); // The latest news article

    const fetchNews = async () => {
      try {
        const response = await axios.get("https://news-web-79f6.onrender.com"); // REPLACE WITH YOUR API URL
        newsList.value = response.data;

        // Assign the latest news (first in the array)
        if (newsList.value.length > 0) {
          latestNews.value = newsList.value[0];
          newsList.value = newsList.value.slice(1); // Remove the latest from the list
        }
      } catch (error) {
        console.error("Error fetching news:", error);
      }
    };

    onMounted(fetchNews);

    return { newsList, latestNews };
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