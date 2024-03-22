<template>
  <header @mouseleave="isFinance='hidden', isUser='hidden'">
    <div class="wrapper">
      <div>
        <nav class="navbar navbar-expand-lg nav-div">
          <div class="container-fluid">
            <div>
              <RouterLink 
              to="/"
              class="navbar-brand"
              >
              <img class="logo-img" src="@/assets/main.jpg" alt="">
              </RouterLink>
            </div>
            <div class="d-flex flex-row justify-content-around flex-grow-1">
              <div 
                class="d-flex flex-row justify-content-around align-items-center flex-grow-1 position-relative"
                @mouseover="isFinance='visible', isUser='hidden'"
              >
                <RouterLink class="py-3 link-dark text-decoration-none fs-4" to="/finance">금융 상품 비교</RouterLink>
                <div
                  class="d-flex flex-row justify-content-center position-absolute top-100 bottom-0"
                  :style="{ visibility: isFinance }"
                >
                  <RouterLink class="mx-3 link-dark text-decoration-none" :to="{ name: 'deposit' }">저축 상품</RouterLink>
                  <RouterLink class="mx-3 link-dark text-decoration-none" :to="{ name: 'personal' }">대출 상품</RouterLink>
                  <RouterLink class="mx-3 link-dark text-decoration-none" :to="{ name: 'exchange' }">환율 정보</RouterLink>
                </div>
              </div>
            
              <div class="d-flex flex-row justify-content-around align-items-center position-relative">
                <img 
                  class="user-img" src="@/assets/user.png" alt=""
                  @mouseover="isUser='visible', isFinance='hidden'"
                >
                <div
                  v-if="store.isLogin"
                  class="d-flex flex-row justify-content-center position-absolute top-100 bottom-0"
                  :style="{ visibility: isUser }"
                >
                  <RouterLink class="mx-2 link-dark text-decoration-none" to="/profile">
                    Profile
                  </RouterLink>
                  <RouterLink class="mx-2 link-dark text-decoration-none" @click="store.logOut" to="/main">
                    LogOut
                  </RouterLink>
                </div>
                <div
                 v-else
                 class="d-flex flex-row justify-content-center position-absolute top-100 bottom-0"
                 :style="{ visibility: isUser }"
                >
                  <RouterLink class="mx-2 link-dark text-decoration-none" to="/signup">
                    SignUp
                  </RouterLink>
                  <RouterLink class="mx-2 link-dark text-decoration-none" to="/login">
                    LogIn
                  </RouterLink>
                </div>
              </div>
            </div>
            <RouterLink @mouseover="isCommu=true" @mouseout="isCommu=false" class="mx-3 link-dark text-decoration-none" to="/community">
              <img v-if="isCommu" class="commu-img" src="@/assets/speaker_move.gif" alt="">
              <img v-else class="commu-img" src="@/assets/speaker.png" alt="">
            </RouterLink>
            <div class="me-2" @click="goSearch" @mouseover="isSearch=true" @mouseout="isSearch=false">
              <img v-if="isSearch" class="search-img" src="@/assets/search_move.gif" alt="">
              <img v-else class="search-img" src="@/assets/search.png" alt="">
            </div>
          </div>
        </nav>
      </div>
    </div>
  </header>
  <div class="d-flex flex-column align-items-center">
    <div class="cont">
      <RouterView />
    </div>
  </div>
</template>


<script setup>
import { useRouter, RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import { ref } from 'vue';
import { computed } from '@vue/reactivity';

const store = useCounterStore()
const router = useRouter()

const isCommu = ref(false)
const isSearch = ref(false)
const isFinance = ref('hidden')
const isUser = ref('hidden')

const goSearch = function () {
  router.push({ name: 'main' })
}

</script>


<style scoped>
* {
  font-family: 'NanumSquareNeoBold';
}
.nav-div {
  height: 90px;
  padding-bottom: 20px;
}
.cont {
  width: 90%;
}
.logo-img {
  width: 200px;
}
.user-img {
  width: 30px;
}
.search-img {
  width: 32px;
  margin-bottom: 5px;
}
.commu-img {
  width: 40px;
}
.sub-navbar {
  opacity: 0.7;
}
</style>
