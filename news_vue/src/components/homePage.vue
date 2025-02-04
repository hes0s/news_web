<template> 
<Navbar/>
</template>

<script> 
import Navbar from '@/views/navbar.vue'

export default {
    name: 'homePage',
  components: {
    Navbar, // Register the component
  },
};
</script>

<style scoped> 
.container { 
    background-color: aqua;
}
</style> 