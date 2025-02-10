<script>
export default {
  name: 'Navbar',
}
import homePage from '../components/homePage.vue'
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-dark-subtle pb-5 ">
    <div class="container-fluid ">
<<<<<<< HEAD
=======
      <a class="navbar-brand" href="#">Navbar</a>
>>>>>>> 4fcea2976ed55e5c6628838deab5f2527571a783
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
<<<<<<< HEAD
            class="btn btn-secondary  mx-2"
=======
            class="navbar-brand btn btn-secondary mx-2"
>>>>>>> 4fcea2976ed55e5c6628838deab5f2527571a783
            type="submit"
            @click="$router.push('/')"
          >
            Home
          </button>
          </li>
        </ul>
        <div class="d-flex container-fluid" id="nav_log">
<<<<<<< HEAD
          <button class="btn btn-secondary mx-2"
            type="submit"
            @click="$router.push('/login')" >Login</button>
=======
          <button class="btn btn-secondary mx-2" type="submit">Login</button>
>>>>>>> 4fcea2976ed55e5c6628838deab5f2527571a783
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
.bg-dark-subtle{
  border-radius: 20px;
}
</style>