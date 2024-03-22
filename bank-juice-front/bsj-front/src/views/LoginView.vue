<template>
  <div class="my-5 d-flex flex-column align-items-center">
    <div class="mb-5 d-flex flex-row justify-content-center">
      <img class="main-img" src="@/assets/main_logo.jpg" alt="">
    </div> 
    <div class="bot-div d-flex flex-column align-items-center">
      <form class="form-div form-control d-flex flex-column" @submit.prevent="logIn">
        <div class="d-flex flex-column mb-3">
          <label class="mx-5 mt-3 mb-1 label-div" for="username">아이디</label>
          <input 
            class="form-control input-div" 
            id="username" 
            type="text"
            v-model.trim="username"
            placeholder="아이디를 입력해주세요."
          >
        </div>
        
        <div class="d-flex flex-column mb-3">
          <label class="mx-5 mt-3 mb-1 label-div" for="password">비밀번호</label>
          <input 
            class="form-control input-div" 
            id="password" 
            type="password"
            v-model.trim="password"
            placeholder="비밀번호를 입력해주세요."
          >        
        </div>
                
        <input class="mt-3 mb-2 btn form-btn" type="submit" value="로그인">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username : username.value,
    password : password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>
.main-img {
  width: 500px;
}
.bot-div {
  width: 500px;
}
.form-div {
  width: 90%;
}
.label-div {
  font-family: 'NanumSquareNeoBold';
  color: black;
  opacity: 0.8;
  font-size: 20px;
}
.input-div {
  align-self: center;
  height: 40px;
  width: 80%;
  font-size: 15px;
  padding-left: 25px;
  border-radius: 10px;
}
.form-btn {
  align-self: center;
  height: 45px;
  width: 70%;
  font-size: 20px;
  background-color: #b2ecc5;
  color: #02b03c;
}
</style>