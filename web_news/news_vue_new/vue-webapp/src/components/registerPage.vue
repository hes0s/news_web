<template>
  <div class="all">
    <Navbar />

  <div class="registrationForm">
    <form>
      <h3>Registration</h3>
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" aria-describedby="emailHelp" />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" />
      </div>
      <div class="mb-3">
        <label for="confirmPassword" class="form-label" alt="confirmPassword"
          >Confirm Password</label
        >
        <input type="password" class="form-control" id="confirmPassword" />
      </div>
    </form>
  </div>
  </div>
</template>

<script>
import Navbar from '../views/navbar.vue'
export default {
  name: 'registerPage',
}
</script>

<style scoped>
.registrationForm {
  background-color: bisque;
  border-radius: 10%;
  margin: 0 auto ;
  width: 500px;
  padding: 50px;
  margin-top: 100px;
}

</style>