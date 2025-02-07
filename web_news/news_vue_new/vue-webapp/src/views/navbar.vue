<script>
export default {
  name: 'Navbar',
}
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
        </ul>
        <div class="d-flex container-fluid" id="nav_log">
          <button class="btn btn-outline-success mx-2" type="submit">Login</button>
          <button
            class="btn btn-outline-success"
            type="submit"
            @click="$router.push('/register')"
          >
            Register
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
#nav_log {
  justify-content: flex-end;
}
</style>
