<template>
  <div>
    <div class="d-flex flex-row justify-content-center">
      <div class="my-4 d-flex flex-row justify-content-around finance-nav">
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'deposit' }">
          <span>예금</span>
        </RouterLink>
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'savings' }">
          <span>적금</span>
        </RouterLink>
      </div>
    </div>
    <br>
    <div class="finance-main">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, RouterLink, RouterView } from 'vue-router';

const route = useRoute()

onMounted(() => {

})

</script>

<style scoped>
.category-div {
  width: 30%;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #b2ecc5;
  color: #02b03c;  
  border-radius: 10px;
}
.category-div:hover {
  width: 30%;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ddf1e4;
  color: #02b03c;  
  border-radius: 10px;
}
.finance-nav {
  width: 80%;
}
</style>