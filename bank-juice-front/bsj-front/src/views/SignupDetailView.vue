<template>
  <div class="my-5 d-flex flex-column align-items-center">
    <div class="mb-5 d-flex flex-row justify-content-center">
      <img class="main-img" src="@/assets/main_logo.jpg" alt="">
    </div> 
    <div class="bot-div d-flex flex-column align-items-center">
      <form class="form-div form-control d-flex flex-column" @submit.prevent="addProfile">
        <div class="d-flex flex-column mb-2">
          <label class="mx-5 mt-3 mb-1 label-div" for="nickname">닉네임</label>
          <input 
            class="form-control input-div" 
            id="nickname" 
            type="text"
            v-model.trim="nickname"
            placeholder="닉네임을 입력해주세요."
          >
        </div>
        <div class="d-flex flex-column mb-2">
          <label class="mx-5 mt-3 mb-1 label-div" for="email">이메일</label>
          <input 
            class="form-control input-div" 
            id="email" 
            type="email"
            v-model.trim="email"
            placeholder="이메일을 입력해주세요."
          >
        </div>
        
        <div class="d-flex flex-column mb-2">
          <label class="mx-5 mt-3 mb-1 label-div" for="age">나이</label>
          <input 
            class="form-control input-div" 
            id="age" 
            type="number"
            v-model.trim="age"
            placeholder="나이를 입력해주세요."
          >        
        </div>
        
        <div class="d-flex flex-column mb-2">
          <label class="mx-5 mt-3 mb-1 label-div" for="gender">성별</label>
          <div id="gender" class="form-control input-div d-flex flex-row justify-content-around">
            <div class="d-flex flex-row align-items-center">
              <label for="male" class="me-2">남자</label>
              <input id="male" type="radio" v-model="gender" value="1" checked>
            </div>
            <div class="d-flex flex-row align-items-center me-3">
              <label for="female" class="me-2">여자</label>
              <input  id="female" type="radio" v-model="gender" value="0">
            </div>
          </div>
        </div>
        
        <div class="d-flex flex-column mb-3">
          <label class="mx-5 mt-3 mb-1 label-div" for="salary">연수입</label>
          <input 
            class="form-control input-div" 
            id="salary" 
            type="number"
            v-model.trim="salary"
            placeholder="연봉 금액을 입력해주세요."
          >     
        </div>
        
        <input class="mt-3 mb-2 btn form-btn" type="submit" value="추가 정보 저장">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()

const nickname = ref(null)
const email = ref(null)
const age = ref(null)
const gender = ref(1)
const salary = ref(null)

const addProfile = function () {
  const payload = {
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    gender: gender.value,
    salary: salary.value
  }
  store.addProfileData(payload)
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