<script>
export default {
  name: 'grid_news',
}
</script>

<template>
  <div class="card mb-3 mx-auto mt-5" style="width: 800px; height: 500px">
    <img src="..." class="card-img-top" alt="..." />
    <div class="card-body">
      <h4 class="card-sub-title">Noutatea zilei</h4>
      <h5 class="card-title">Card title</h5>
      <p class="card-text">
        This is a wider card with supporting text below as a natural lead-in to additional content.
        This content is a little bit longer.
      </p>
      <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
    </div>
  </div>
  <div class="row row-cols-1 row-cols-md-3 g-4 mx-auto" style="width: 800px">
    <div class="col">
      <div class="card h-100">
        <img src="..." class="card-img-top" alt="..." />
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
        <img src="..." class="card-img-top" alt="..." />
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">This is a short card.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="..." class="card-img-top" alt="..." />
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
</template>
