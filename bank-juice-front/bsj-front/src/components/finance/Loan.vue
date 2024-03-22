<template>
  <div>
    <div class="d-flex flex-row justify-content-center">
      <div class="my-4 d-flex flex-row justify-content-around loan-nav">
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'personal' }">
          <span>신용 대출</span>
        </RouterLink>
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'mortgage' }">
          <span>주택 담보 대출</span>
        </RouterLink>
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'jeonse' }">
          <span>전세 대출</span>
        </RouterLink>
      </div>
    </div>
    <br>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, RouterLink, RouterView } from 'vue-router';

const route = useRoute()


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
.loan-nav {
  width: 80%;
}
</style>