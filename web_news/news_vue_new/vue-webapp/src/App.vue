<script setup>
import { ref } from 'vue';
import axios from 'axios';
const message = ref('Hello, Vue!');
axios.get('https://newsweb-production-1f35.up.railway.app')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
</script>

<template>
  <div id="app">
    <router-view /> <!-- If using Vue Router -->
  </div>
</template>
