<template>
  <div>
    <div class="mt-5 detail-div ">
      <img @click="goBack" class="back-img" src="@/assets/back.png" alt="">
      <div class="d-flex flex-row justify-content-between">
        <div class="card-div d-flex flex-column align-items-center">
          <div v-if="personal" class="mt-1 mb-6 recommend-div">
            <div>
              <div>
                <div class="card my-2 p-4 d-flex flex-column">
                  <div class="d-flex flex-row justify-content-between">
                    <div class="title">
                      <h2 class="mb-4">{{ personal.fin_prdt_nm }}</h2>
                      <span class="my-4">은행 : {{ personal.kor_co_nm }}</span>
                      <p class="mt-3 mb-3">가입 방법 : {{ personal.join_way }}</p>
                    </div>
                    <div class="rate d-flex flex-column justify-content-around">
                      <div>
                        <span class="mt-2 text-gray">최고</span>
                        <span class=fs-4>
                          연 {{ highest_rate }} %
                        </span>
                      </div>
                      <div>
                        <span class="mt-2 text-gray">최저</span>
                        <span class="fs-4">
                        연 {{ lowest_rate }} % 
                        </span>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex flex-row justify-content-end">
                    <div v-if="isSaved">
                      <button @click="productSave" class="btn btn-color1 ">내 상품 취소</button>
                    </div>
                    <div v-else>
                      <button @click="productSave" class="btn btn-color1">내 상품 담기</button>
                    </div>
                    <a :href="bank_info.homp_url"><button class="btn mx-2 btn-color2">공식홈에서 더 알아보기</button></a>
                  </div>
                </div>

                <div>
                  <div class="card p-4">
                    <h3>금리 안내</h3>
                    <div>
                      <div class="mt-2">
                        <div class="d-flex flex-row justify-content-between">
                          <p>신용 점수 별 금리</p>
                          <p>금리 유형 : {{ option1.crdt_lend_rate_type_nm }}</p>
                        </div>

                        <table class="table border text-center text-gray" style="height: 100px;">
                          <thead>
                            <tr style="background-color : rgba(251, 251, 251, 0.889);">
                              <th style="width: 40%;border-right:solid 1px lightgray ">신용 점수</th>
                              <th>금리</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-if="option1.crdt_grad_1" >
                              <td style="border-right: 1px solid lightgray ">900점 이상</td>
                              <td>{{ option1.crdt_grad_1 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_4" >
                              <td style="border-right: 1px solid lightgray ">801 ~ 900 점</td>
                              <td>{{ option1.crdt_grad_4 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_5" >
                              <td style="border-right: 1px solid lightgray ">701 ~ 800 점</td>
                              <td>{{ option1.crdt_grad_5 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_6" >
                              <td style="border-right: 1px solid lightgray ">601 ~ 700 점</td>
                              <td>{{ option1.crdt_grad_6 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_10" >
                              <td style="border-right: 1px solid lightgray ">501 ~ 600 점</td>
                              <td>{{ option1.crdt_grad_10 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_11" >
                              <td style="border-right: 1px solid lightgray ">401 ~ 500 점</td>
                              <td>{{ option1.crdt_grad_11 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_12" >
                              <td style="border-right: 1px solid lightgray ">301 ~ 400 점</td>
                              <td>{{ option1.crdt_grad_12 }} %</td>
                            </tr>
                            <tr v-if="option1.crdt_grad_13" >
                              <td style="border-right: 1px solid lightgray ">300 점 미만</td>
                              <td>{{ option1.crdt_grad_13 }} %</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
        <div class="side-div mt-3 mb-6">
          <KakaoMap :bank-name="personal.kor_co_nm" v-if="personal" class="kakao-map"/>
          <div class="mt-2">
            <div>
              <h5 class="mt-4 mb-2 top-text">유사한 상품</h5>
              <div class="card my-2 p-2" v-for="pdt, idx in recommended_products_sliced" :key="pdt.id">
                <div class="d-flex flex-column" @click="goDetail(pdt.id)">
                  <p class="my-1 top-text">{{ pdt.kor_co_nm }}</p>
                  <p class="my-2 bot-text">{{ pdt.fin_prdt_nm }}</p>
                </div>  
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch  } from 'vue';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
import KakaoMap from '@/components/finance/finance_list/KakaoMap.vue'
import Swal from 'sweetalert2'

const route = useRoute()
const store = useCounterStore()
const router = useRouter()

const personal = ref(null)
const bank_info = ref(null)
const opts = ref(null)
const option1 = ref(null)
const recommended_products = ref([])
const isSaved = ref(false)
const rate = ref(0)
const highest_rate = ref(true)
const lowest_rate = ref(false)
const cal_amount = ref(10000000)
const beforeInterest = computed(()=>{
  return cal_amount.value * rate.value 
})

// 유사한 상품 출력
const recommended_products_sliced = computed(()=>{
  let arr = []
  for (let i = 0 ; i < recommended_products.value.length ; i ++) {
    if (recommended_products[i]=== personal.value.fin_prdt_nm ) {
      continue
    }    
    arr.push(recommended_products.value[i])
  }
  if (arr.length > 5) {
    return arr.slice(0, 5)
  }
})


// 뒤로 가기
const goBack = function () {
  router.push({ name: 'personal' })
}

//페이지 이동
const goDetail = function (personalPk) {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/personal/${personalPk}/`,
  })
  .then((res) => {
      console.log(res.data)
      personal.value = res.data
      opts.value = res.data.options
      option1.value = res.data.options[0]
      lowest_rate.value = saveMinRate(option1.value)
      highest_rate.value = saveMaxRate(option1.value)
      const options = res.data.options
    })
    // 로컬 스토리지에 최근 본 상품 저장
    .then((res) => {
      if (!store.recent_personal == null) {
        const find_personal = store.recent_personal.find((depo) => depo.id == personal.value.id)
        if (store.recent_personal.length === 5) {
          if (!find_personal) {
            store.recent_personal.shift()
            store.recent_personal.push(personal.value)
          }
        } else {
          if (!find_personal) {
            store.recent_personal.push(personal.value)
          }
        }
      } else {
        store.recent_personal = [personal.value]
      }
    })
    //은행 정보
    .then((res)=>{
      // console.log(deposit.value)
      axios({
        method : 'get',
        url : `${store.API_URL}/info/bank/${personal.value.bank}/`
      })
        .then((res)=>{
          // console.log(res.data.homp_url)
          bank_info.value = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
      })
    .then((res)=>{
      axios({
        method:'get',
        url : `${store.API_URL}/info/user_join_personal/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
      })
      .then((res)=>{
        res.data.forEach((ele, idx) => {
          if (ele.id === personal.value.id) {
            isSaved.value = true
          } else {
            isSaved.value = false
          }
        })
      })
    })
    .then((res)=>{
      axios({
        method:'get',
        url:`${store.API_URL}/info/personal_save/${personalPk}/`
      })
      .then((res)=>{
        recommended_products.value = res.data
      })
      .then((res)=>{
        router.push({ name: 'personalDetail', params: { pk: personalPk } })
      })
    })
    .catch((err) => {
      console.log(err)
    })
}


const converted_amount = computed(()=>{
  return cal_amount.value/10000
})

const calculate = function (r) {
  rate.value = r
  console.log(event)
  if (event.target.id === 'highest') {
    highest_rate.value = true
    default_rate.value = false
  } else if (event.target.id === 'default'){
    highest_rate.value = false
    default_rate.value = true
  }
}

//상품 저장 버튼
const productSave = function(event) {
  axios({
    method:'post',
    url: `${store.API_URL}/info/personal_save/${route.params.pk}/`,
    headers: {
          Authorization: `Token ${store.token}`
        }
  })
  .then((res)=>{
    // console.log(res.data)
    if(res.data.message === '저장취소') {
      isSaved.value = false
    } else {
      isSaved.value = true
    }
  })
  .catch((err)=>{
    Swal.fire({
      title: 'Warning!',
      text: '로그인이 필요합니다!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: '로그인',
      cancelButtonText: '닫기',
    }) .then((result) => {
      if (result.isConfirmed){
        router.push({name: 'login'})
      }
    })
    console.log(err)
  })
}

const saveMinRate = function (option) {
  if (option.crdt_grad_1) {
    return option.crdt_grad_1
  } else if (option.crdt_grad_4) {
    return option.crdt_grad_4
  } else if (option.crdt_grad_5) {
    return option.crdt_grad_5
  } else if (option.crdt_grad_6) {
    return option.crdt_grad_6
  } else if (option.crdt_grad_10) {
    return option.crdt_grad_10
  } else if (option.crdt_grad_11) {
    return option.crdt_grad_11
  } else if (option.crdt_grad_12) {
    return option.crdt_grad_12
  } else if (option.crdt_grad_13) {
    return option.crdt_grad_13
  } 
}

const saveMaxRate = function (option) {
  if (option.crdt_grad_13) {
    return option.crdt_grad_13
  } else if (option.crdt_grad_12) {
    return option.crdt_grad_12
  } else if (option.crdt_grad_11) {
    return option.crdt_grad_11
  } else if (option.crdt_grad_10) {
    return option.crdt_grad_10
  } else if (option.crdt_grad_6) {
    return option.crdt_grad_6
  } else if (option.crdt_grad_5) {
    return option.crdt_grad_5
  } else if (option.crdt_grad_4) {
    return option.crdt_grad_4
  } else if (option.crdt_grad_1) {
    return option.crdt_grad_1
  } 
}

const reload = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/personal/${route.params.pk}/`,
  })
  .then((res) => {
      console.log(res.data)
      personal.value = res.data
      opts.value = res.data.options
      option1.value = res.data.options[0]
      lowest_rate.value = saveMinRate(option1.value)
      highest_rate.value = saveMaxRate(option1.value)
      const options = res.data.options
    })
    // 로컬 스토리지에 최근 본 상품 저장
    .then((res) => {
      if (!store.recent_personal == null) {
        const find_personal = store.recent_personal.find((depo) => depo.id == personal.value.id)
        if (store.recent_personal.length === 5) {
          if (!find_personal) {
            store.recent_personal.shift()
            store.recent_personal.push(personal.value)
          }
        } else {
          if (!find_personal) {
            store.recent_personal.push(personal.value)
          }
        }
      } else {
        store.recent_personal = [personal.value]
      }
    })
    //은행 정보
    .then((res)=>{
      // console.log(deposit.value)
      axios({
        method : 'get',
        url : `${store.API_URL}/info/bank/${personal.value.bank}/`
      })
        .then((res)=>{
          // console.log(res.data.homp_url)
          bank_info.value = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
      })
    .then((res)=>{
      axios({
        method:'get',
        url : `${store.API_URL}/info/user_join_personal/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
      })
      .then((res)=>{
        res.data.forEach((ele, idx) => {
          if (ele.id === personal.value.id) {
            isSaved.value = true
          } else {
            isSaved.value = false
          }
        })
      })
    })
    .catch((err) => {
      console.log(err)
    })
    axios({
      method:'get',
      url:`${store.API_URL}/info/personal_save/${route.params.pk}/`
    })
    .then((res)=>{
      recommended_products.value = res.data
    })
}
onMounted(() => {
  reload() 
})

</script>

<style scoped>
.detail-div {
  width: 100%;
}

.card-div {
  width: 65%;
  height: 800px;
  /* background-color: red; */
}
.recommend-div {
  width: 90%;
}
.side-div {
  width: 30%;
  height: 800px;
  /* background-color: blue; */
}
input[type=number]{
  height: 50px;
  width: 60%;
  background-color:rgb(233, 233, 233);
  border : none;
  border-radius: 10px;
  padding-left : 10px;
  /* position : relative; */
}
.description {
  font-size : 15px;
  color : gray;
}
.result-div { 
  background-color: #e8fbee;
}
.result-click{
  width: 100%;
}
.won {
  margin-left : -48px;
}
.btn-color1{
  background-color: #00C743;
  color : white;
}
.btn-color2{
  background-color: #b2ecc5;
  color: #02b03c;
}

.btn:hover{
  background-color: #b2ecc5;
  color : black;
}
.selected{
  border : 1px solid #5b966e;
}
.text-gray {
  color : gray; 
}
.font-color-green {
  color : #03aa3b;
  font-weight: bold;
}
.title {
  width: 60%;
}
.rate {
  width: 30%;
}

.back-img {
  width: 40px;
  transform: scaleX(-1);
  opacity: 0.8;
  margin-left: 30px;
}
.top-text {
  color: gray;
  opacity: 0.8;
  font-size: 15px;
}
.bot-text {
  font-size: 18px;
}
</style>