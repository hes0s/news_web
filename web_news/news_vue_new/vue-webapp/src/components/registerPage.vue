<template>
  <div class="all">
  <navbar />                                                                                                                                                                                                                                              

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
      <div class="mb3">
      <button class="btn btn-secondary mx-2 btn-lg hw" type="submit">Confirm</button>
    </div>
    </form>
  </div>
  </div>
</template>

<script>
import navbar from '../views/navbar.vue'
export default {
  components: { navbar },
  name: 'registerPage',
}
</script>

<style scoped>
.registrationForm {
  background-color: gray;
  border-radius: 10%;
  margin: 0 auto ;
  width: 500px;
  padding: 50px;
  margin-top: 100px;
}
.hw{
      margin: auto;
      width: 380px;
}
</style>