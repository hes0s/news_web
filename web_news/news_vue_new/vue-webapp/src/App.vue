<script setup>
import { ref } from 'vue';
axios.get("https://your-backend.railway.app/news")
const message = ref('Hello, Vue!');
</script>

<template>
  <div id="app">§
    <router-view /> <!-- If using Vue Router -->
  </div>
</template>
