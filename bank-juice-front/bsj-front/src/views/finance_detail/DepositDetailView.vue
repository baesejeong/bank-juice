<template>
  <div>
    <div class="mt-5 detail-div ">
      <img @click="goBack" class="back-img" src="@/assets/back.png" alt="">
      <div class="d-flex flex-row justify-content-between">
        <div class="card-div d-flex flex-column align-items-center">
          <div v-if="deposit" class="mt-1 mb-6 recommend-div">
            <div>
              <div>
                <div class="card my-2 p-4 d-flex flex-column">
                  <div class="d-flex flex-row justify-content-between">
                    <div class="title">
                      <h2 class="mb-4">{{ deposit.fin_prdt_nm }}</h2>
                      <span class="my-4">은행 : {{ deposit.kor_co_nm }}</span>
                      <p class="mt-3 mb-3">가입 방법 : {{ deposit.join_way }}</p>
                    </div>
                    <div class="rate d-flex flex-column justify-content-around">
                      <div>
                        <span class="mt-2 text-gray" >최고</span>
                        <span class="fs-4">
                          연 {{ option_12.intr_rate2 }} %
                        </span>
                      </div>
                      <div>
                        <span class="mt-2 text-gray">기본</span>
                        <span class="fs-4">
                          연 {{ option_12.intr_rate }} % 
                        </span>
                      </div>
                      <div class="mb-4">
                        <span style="color: gray">
                          ({{ option_12.save_trm }}개월, 세전)
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
                  
                  <a :href="bank_info"><button class="btn mx-2 btn-color2">공식홈에서 더 알아보기</button></a>
                </div>
              </div>
                <div>
                    <div class="card my-2 p-4">
                      <h5 class="fw-bolder">상품 안내</h5>
                      <div class="mt-2">
                        
                        <div class="my-2">
                          <span class="text-gray">
                            가입대상 
                          </span>
                          <span class="mx-2">
                            {{ deposit.join_member }}
                          </span>
                        </div>
                        <div class="my-2">
                          <span class="text-gray">
                            가입방법 
                          </span>
                          <span class="mx-2">
                          {{ deposit.join_way }}
                          </span>
                        </div>

                        <details>
                          <summary class="text-gray">더보기</summary>
                        <div class="mt-2">
                          <div class="my-2">
                            <span class="text-gray">
                              만기 후 이자율 
                            </span>
                            <span class="mx-2">
                              {{ deposit.mtrt_int }}
                            </span>
                          </div>
                          <div class="my-2">
                            <span class="text-gray">
                              우대조건
                            </span>
                            <span class="mx-2">
                              {{ deposit.spcl_cnd }}
                            </span>
                          </div>
                          <div class="my-2">
                            <span class="text-gray">
                              기타 유의사항
                            </span>
                            <span class="mx-2">
                              {{ deposit.etc_note }}
                            </span>
                          </div>
                        </div>
                        </details>
                    </div>
                    </div>
                    <div class="card p-4">
                      <h3>금리 안내</h3>
                      <div class="pt-2 px-1">
                        <label for="cal_amount" >예치 금액</label>
                      </div>
                      <div class="d-flex">
                        <input type="number" v-model="cal_amount" id="cal_amount" class="fs-4">
                        <span class="fs-3 mt-1 won">원</span>
                        <vue-number-format
                          class="description mt-3 m-4 pl-2 fs-5 number text-start"
                          :value="converted_amount" 
                          :options="{ 
                            thousand: ',',
                            decimal: '.',
                            prefix: '',
                            precision: 0,
                            suffix: ' 만원',
                            }"
                          >
                        </vue-number-format>
                      </div>
                      <div>
                        <div>
                          <div class="d-flex result-click text-center" style="height: 40px;">
                          <div @click="calculate(option_12.intr_rate2)" style="width: 100%; " id="highest" :class="[ highest_rate? 'selected' :'border', 'pt-2',]">최고 금리 {{ option_12.intr_rate2 }} %</div>
                          <div @click="calculate(option_12.intr_rate)" style="width: 100%" id="default" :class="[ default_rate? 'selected' :'border', 'pt-2',]">기본 금리  {{ option_12.intr_rate }} % </div>
                        </div>
                        <div class="result-div"> 
                          <div class="d-flex justify-content-between">
                            <span class="m-2 text-gray">
                              원금합계 
                            </span>
                            <vue-number-format
                                class="number-form text-end m-2"
                                :value="cal_amount" 
                                :options="{ 
                                  thousand: ',',
                                  decimal: '.',
                                  prefix: '',
                                  precision: 0,
                                  suffix: ' 원',
                                  }"
                              >
                            </vue-number-format>
                          </div>
                          <div class="d-flex justify-content-between">
                            <span class="m-2 text-gray">
                              세전이자 
                            </span>
                            <vue-number-format
                                class="number-form text-end m-2"
                                :value="beforeInterest" 
                                :options="{ 
                                  thousand: ',',
                                  decimal: '.',
                                  prefix: '',
                                  precision: 0,
                                  suffix: ' 원',
                                  }"
                              >
                            </vue-number-format>
                          </div>
                          <div>
                            <div class="d-flex justify-content-between">
                              <span class="m-2 text-gray fs-6">
                                이자과세(15.4%)
                              </span>
                              <vue-number-format
                                class="number-form text-end m-2"
                                :value="beforeInterest*0.0154" 
                                :options="{ 
                                  thousand: ',',
                                  decimal: '.',
                                  prefix: '',
                                  precision: 0,
                                  suffix: ' 원',
                                  }"
                              >
                              </vue-number-format>
                            </div>
                            <div style="width: 100% height: 1px;" class="mx-2">
                              <hr style="width: 100%" class="my-0">
                            </div>
                          </div>
                          
                          <div class="d-flex justify-content-between">
                            <span class="p-2 text-gray">
                              세후 수령액 
                            </span>
                            <vue-number-format
                              class="number-form text-end m-2 fs-5  font-color-green"
                              :value="cal_amount + beforeInterest - beforeInterest * 0.0154" 
                              :options="{ 
                                thousand: ',',
                                decimal: '.',
                                prefix: '',
                                precision: 0,
                                suffix: ' 원',
                                }"
                            >
                            </vue-number-format>
                          </div>
                          </div>
                        </div>
                        <div class="mt-5">
                          <p>기간별 금리</p>
                          <table class="table border text-center text-gray" style="height: 100px;">
                            <tr style="background-color : rgba(251, 251, 251, 0.889);">
                              <th style="width: 40%;border-right:solid 1px lightgray ">기간</th>
                              <th>금리</th>
                            </tr>
                            
                            <tr v-for="opt in opts">
                              <td style="border-right: 1px solid lightgray ">{{ opt.save_trm }}개월</td>
                              <td>{{ opt.intr_rate ? opt.intr_rate : opt.intr_rate2 }}</td>
                            </tr>
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
          <KakaoMap :bank-name="deposit.kor_co_nm" v-if="deposit" class="kakao-map" style="width: 100%;"/>
          <div class="mt-2">
            <div>
              <h5 class="mt-4 mb-2 top-text">유사한 상품</h5>
              <div 
                class="card my-2 p-2" v-for="pdt, idx in recommended_products_sliced" 
                :key="pdt.id"
                @click="goDetail(pdt.id)"
              >
                <div class="d-flex flex-column">
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
import { onBeforeRouteUpdate, useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
import KakaoMap from '@/components/finance/finance_list/KakaoMap.vue'
import VueNumberFormat from 'vue-number-format'
import Swal from 'sweetalert2'

const route = useRoute()
const store = useCounterStore()
const router = useRouter()

const deposit = ref(null)
const bank_info = ref(null)
const opts = ref(null)
const option_12 = ref(null)
const recommended_products = ref([])
const isSaved = ref(false)
const rate = ref(0)
const highest_rate = ref(true)
const default_rate = ref(false)
const cal_amount = ref(10000000)
const beforeInterest = computed(()=>{
  return cal_amount.value * rate.value * 0.01
})



const recommended_products_sliced = computed(()=>{
  let arr = []
  for (let i = 0 ; i < recommended_products.value.length ; i ++) {  
    arr.push(recommended_products.value[i])
  }
  // console.log(arr)
  if (arr.length > 5) {
    // console.log(arr)
    return arr.slice(0, 5)
  }
})
const converted_amount = computed(()=>{
  return cal_amount.value/10000
})
const calculate = function (r) {
  rate.value = r
  if (event.target.id === 'highest') {
    highest_rate.value = true
    default_rate.value = false
  } else if (event.target.id === 'default'){
    highest_rate.value = false
    default_rate.value = true
  }
}
// 뒤로 가기
const goBack = function () {
  router.go(-1)
}
//페이지 이동
const goDetail = function (depositPk) {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/deposit/${depositPk}/`,
  })
    .then((res) => {
      deposit.value = res.data
      opts.value = res.data.options

      const options= res.data.options

      const option_list= filter_save_trm(options)

      if(option_list.length > 0) {

        option_12.value = option_list[0]
        rate.value = option_12.value.intr_rate2
      }
      else {

        options.forEach((option, idx)=>{
          // console.log(option)
          if (option.save_trm === '6' & (option_12.value === null | option_12.value > option.save_trm)) {
            option_12.value = option
            rate.value = option_12.value.intr_rate2
          }
          else if (option.save_trm === '24' & (option_12.value === null | option_12.value > option.save_trm)) {
            option_12.value = option
            rate.value = option_12.value.intr_rate2
          }
          else if (option.save_trm === '36' & option_12.value === null) {
            option_12.value = option
            rate.value = option_12.value.intr_rate2
          }
        })

      }
    })
    
    //은행 정보
    .then((res)=>{
      // console.log(deposit.value)
      axios({
        method : 'get',
        url : `${store.API_URL}/info/bank/${deposit.value.bank}/`
      })
        .then((res)=>{
          // console.log(res.data.homp_url)
          bank_info.value = res.data.homp_url
        })
        .catch((err)=>{
          console.log(err)
        })
    })
    .then((res)=>{
      axios({
        method:'get',
        url : `${store.API_URL}/info/user_join_deposit/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
      })
      .then((res)=>{
        console.log(res.data)

        res.data.forEach((ele, idx) => {
          if (ele.id === deposit.value.id) {
            isSaved.value = true
          } else {
            isSaved.value = false
          }
        })
      })
    })
    .then((res) => {
      axios({
        method:'get',
        url:`${store.API_URL}/info/deposit_save/${depositPk}/`
      })
      .then((res)=>{
        console.log(res.data)
        recommended_products.value = res.data
      })
      .then((res) => {
        router.push({ name: 'depositDetail', params: { pk: depositPk } })
      })
    })
    .catch((err) => {
      console.log(err)
      console.log(1)
    })
  // console.log(router)
  // router.go(0)
}



// 추천 상품 필터링
const filter_save_trm= function (options) {
        return options.filter((options)=> options.save_trm === '12')
    }

// 
// router.beforeEach((to, from)=>{
//   // console.log(to, from)
//   reload()
//   // router.go(0)
//   }
// )

//상품 저장 버튼
const productSave = function(event) {
  axios({
    method:'post',
    url: `${store.API_URL}/info/deposit_save/${route.params.pk}/`,
    headers: {
          Authorization: `Token ${store.token}`
        }
  })
  .then((res)=>{
    // console.log('*', res.data)
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

const reload = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/deposit/${route.params.pk}/`,
  })
    .then((res) => {
      deposit.value = res.data
      opts.value = res.data.options

      const options= res.data.options

      const option_list= filter_save_trm(options)

      if(option_list.length > 0) {

        option_12.value = option_list[0]
        rate.value = option_12.value.intr_rate2
      }
      else {

        options.forEach((option, idx)=>{
          // console.log(option)
          if (option.save_trm === '6' & (option_12.value === null | option_12.value > option.save_trm)) {
            option_12.value = option
            rate.value = option_12.value.intr_rate2
          }
          else if (option.save_trm === '24' & (option_12.value === null | option_12.value > option.save_trm)) {
            option_12.value = option
            rate.value = option_12.value.intr_rate2
          }
          else if (option.save_trm === '36' & option_12.value === null) {
            option_12.value = option
            rate.value = option_12.value.intr_rate2
          }
        })

      }
    })
    
    //은행 정보
    .then((res)=>{
      // console.log(deposit.value)
      axios({
        method : 'get',
        url : `${store.API_URL}/info/bank/${deposit.value.bank}/`
      })
        .then((res)=>{
          // console.log(res.data.homp_url)
          bank_info.value = res.data.homp_url
        })
        .catch((err)=>{
          console.log(err)
        })
    })
    .then((res)=>{
      axios({
        method:'get',
        url : `${store.API_URL}/info/user_join_deposit/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
      })
      .then((res)=>{
        console.log(res.data)

        res.data.forEach((ele, idx) => {
          if (ele.id === deposit.value.id) {
            isSaved.value = true
          } else {
            isSaved.value = false
          }
        })
      })
    })
    .catch((err) => {
      console.log(err)
      console.log(1)
    })



    axios({
      method:'get',
      url:`${store.API_URL}/info/deposit_save/${route.params.pk}/`
    })
    .then((res)=>{
      console.log(res.data)
      recommended_products.value = res.data
    })
}
onMounted(() => {
  reload()
  console.log(store.recent_deposit == null)
  if (!store.recent_deposit == null) {
    const find_deposit = store.recent_deposit.find((depo) => depo.id == deposit.value.id)
    if (store.recent_deposit.length === 5) {
      if (!find_deposit) {
        store.recent_deposit.shift()
        store.recent_deposit.push(deposit.value)
      }
    } else {
      if (!find_deposit) {
        store.recent_deposit.push(deposit.value)
      }
    }
  } else {
    store.recent_deposit = [deposit.value]
  }
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
.number-form {
  border: none;
  background-color: #e8fbee;
}
.number {
  border: none;
}
</style>