<script setup>
import { ref } from 'vue';

const message = ref('Hello, Vue!');
</script>

<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <router-view /> <!-- If using Vue Router -->
  </div>
</template>

<style>
#app {
  text-align: center;
  font-family: Arial, sans-serif;
}
</style>
