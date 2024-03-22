<template>
  <div>
    <div class="d-flex flex-row justify-content-center">
      <div class="my-4 d-flex flex-row justify-content-around profile-nav">
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'myjoin' }">
          <span>내 가입 상품</span>
        </RouterLink>
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'myrecommend' }">
          <span>상품 추천 받기</span>
        </RouterLink>
        <RouterLink class="category-div text-decoration-none" :to="{ name: 'myupdate' }">
          <span>회원 정보 수정</span>
        </RouterLink>
      </div>
    </div>
    <br>
    <RouterView />
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';
import { ref, onMounted } from 'vue';
import { useRoute, RouterLink, RouterView } from 'vue-router';


const store = useCounterStore()
const route = useRoute()


onMounted(() => {
  store.recommended_deposit()
  store.recommended_savings()
  store.recommended_personal()
  store.recommended_mortgage()
  store.recommended_jeonse()
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
.profile-nav {
  width: 80%;
}
</style>