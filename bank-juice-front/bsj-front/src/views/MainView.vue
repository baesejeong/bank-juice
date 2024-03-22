<template>
  <div class="my-5">
    <div class="mb-5 d-flex flex-row justify-content-center">
      <img class="main-img" src="@/assets/main_logo.jpg" alt="">
    </div> 
    <div class="search-div d-flex flex-column">
      <Search/>
    </div>
  </div>
</template>

<script setup>
import Search from '@/components/Search.vue'
</script>

<style scoped>
.main-img {
  width: 500px;
}
* {
  font-family: 'NanumSquareNeoBold';
}
</style>