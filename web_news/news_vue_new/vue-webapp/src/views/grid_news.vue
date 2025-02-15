<script>
export default {
  name: 'GridNews',
}

import { ref, onMounted } from "vue";
import { fetchPhotos, addPhoto } from "@/services/photoService";

const photos = ref([]);
onMounted(loadPhotos);
</script>

<template>
  <div class="all">
    <div v-if="latestPhoto" class="card mb-3 mx-auto mt-5" style="width: 800px; height: 500px">
    <img :src="latestPhoto.photo" class="card-img-top" alt="Photo" />
    <div class="card-body">
      <h4 class="card-sub-title">Noutatea zilei</h4>
      <h5 class="card-title">{{ latestPhoto.name }}</h5>
      <p class="card-text">{{ latestPhoto.description }}</p>
      <p class="card-text"><small class="text-body-secondary">Last updated just now</small></p>
    </div>
  </div>
  <div class="row row-cols-1 row-cols-md-3 g-4 mx-auto" style="width: 800px">
    <div class="col">
      <div class="card h-100">
        <img src="./aboba.jpg" class="card-img-top" />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural lead-in to additional
            content. This content is a little bit longer.
          </p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="./aboba.jpg" class="card-img-top"/>
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">This is a short card.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="./aboba.jpg" class="card-img-top"/>
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">
            This is a longer card with supporting text below as a natural lead-in to additional
            content.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
