<template>
  <div class="mt-4"> 
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, useRoute, RouterView } from 'vue-router';
import { ref, onMounted } from 'vue';

const route = useRoute()

onMounted(() => {
})


</script>


<style scoped>
.finance-main-div {
  margin-top: 40px;
}
</style>