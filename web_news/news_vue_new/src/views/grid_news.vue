<template>
  <div class="all">
    <!-- Highlight the Latest News -->
    <div  class="card mb-3 mx-auto mt-5" style="width: 800px; height: 500px">
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
      <div class="col">
        <div class="card h-100">
          <img src="./aboba.jpg" class="card-img-top" alt="News Photo" />
          <div class="card-body">
            <h5 class="card-title">Title</h5>
            <p class="card-text">Text</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GridNews"}
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