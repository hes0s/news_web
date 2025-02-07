<template>
  <Navbar />
  <h3>Registration</h3>
  <div class="registrationForm">
    <form>
      <div class="mb-3">
        <h3>Registration</h3>
      </div>
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" aria-describedby="emailHelp" />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" />
        <div id="emailHelp" class="form-text" style="color: white">
          We'll never share your email with anyone else.
        </div>
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
      <div class="mb-3">
        <h4>Or use provided methods</h4>
      </div>
    </form>
  </div>
</template>

<script>
import Navbar from '../views/navbar.vue'
export default {
  name: 'registerPage',
}
</script>
