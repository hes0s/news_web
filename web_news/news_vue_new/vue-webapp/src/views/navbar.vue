<script>
export default {
  name: 'Navbar',
}
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-dark-subtle pb-2 rounded-bottom">
    <div class="container-fluid ">
      <button
        class="navbar-toggler bg-light-subtle"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse bg-dark-subtle" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="navbar-band" id="nav_log">
          <button
            class="btn btn-secondary  mx-2"
            type="submit"
            @click="$router.push('/')"
          >
            Home
          </button>
          </li>
        </ul>
        <div class="d-flex container-fluid" id="nav_log">
          <button class="btn btn-secondary mx-2"
            type="submit"
            @click="$router.push('/login')" >Login</button>
          <button
            class="btn btn-secondary mx-2"
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