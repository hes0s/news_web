<script setup>
import { ref } from 'vue';
const message = ref('Hello, Vue!');
</script>
<template>
  <div id="app">
    <router-view /> <!-- If using Vue Router -->
  </div>
</template>
