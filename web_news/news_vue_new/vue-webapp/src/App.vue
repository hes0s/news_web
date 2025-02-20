<script setup>
import { ref } from 'vue';
import axios from 'axios';
const message = ref('Hello, Vue!');
axios.get('https://your-backend.railway.app/news')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
</script>

<template>
  <div id="app">§
    <router-view /> <!-- If using Vue Router -->
  </div>
</template>
