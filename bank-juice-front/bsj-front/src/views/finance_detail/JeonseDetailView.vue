<template>
  <div>
    <div class="mt-5 detail-div ">
      <img @click="goBack" class="back-img" src="@/assets/back.png" alt="">
      <div class="d-flex flex-row justify-content-between">
        <div class="card-div d-flex flex-column align-items-center">
          <div v-if="jeonse" class="mt-1 mb-6 recommend-div">
            <div>
              <div>
                <div class="card my-2 p-4 d-flex flex-column">
                  <div class="d-flex flex-row justify-content-between">
                    <div class="title">
                      <h2 class="mb-4">{{ jeonse.fin_prdt_nm }}</h2>
                      <span class="my-4">은행 : {{ jeonse.kor_co_nm }}</span>
                      <p class="mt-3 mb-3">가입 방법 : {{ jeonse.join_way }}</p>
                    </div>
                    <div class="rate d-flex flex-column justify-content-around">
                      <div>
                        <span class="mt-2 text-gray">최고</span>
                        <span class=fs-4>
                          연 {{ option1.lend_rate_max }} %
                        </span>
                      </div>
                      <div>
                        <span class="mt-2 text-gray">최저</span>
                        <span class="fs-4">
                        연 {{ option1.lend_rate_min }} % 
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
                        <p>금리 적용 방식 / 상환 방식 별 금리</p>
                        <table class="table border text-center text-gray" style="height: 100px;">
                          <thead>
                            <tr style="background-color : rgba(251, 251, 251, 0.889);">
                              <th style="width: 40%;border-right:solid 1px lightgray ">금리 적용 방식</th>
                              <th style="width: 40%;border-right:solid 1px lightgray ">상환 방식</th>
                              <th>최고 금리</th> 
                              <th>최저 금리</th> 
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="option in opts">
                              <td style="border-right: 1px solid lightgray ">{{ option.lend_rate_type_nm }}</td>
                              <td style="border-right: 1px solid lightgray ">{{ option.rpay_type_nm }}</td>
                              <td>{{ option.lend_rate_max }} %</td>
                              <td>{{ option.lend_rate_min }} %</td>
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
          <KakaoMap :bank-name="jeonse.kor_co_nm" v-if="jeonse" class="kakao-map"/>
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

const jeonse = ref(null)
const bank_info = ref(null)
const opts = ref(null)
const option1 = ref(null)
const recommended_products = ref([])
const isSaved = ref(false)
const rate = ref(0)
const cal_amount = ref(10000000)
const beforeInterest = computed(()=>{
  return cal_amount.value * rate.value 
})

// 유사한 상품 출력
const recommended_products_sliced = computed(()=>{
  let arr = []
  for (let i = 0 ; i < recommended_products.value.length ; i ++) {
    if (recommended_products[i]=== jeonse.value.fin_prdt_nm ) {
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
  router.push({ name: 'jeonse' })
}

//페이지 이동
const goDetail = function (jeonsePk) {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/jeonse/${jeonsePk}/`,
  })
  .then((res) => {
      console.log(res.data)
      jeonse.value = res.data
      opts.value = res.data.options
      option1.value = res.data.options[0]
    })
    // 로컬 스토리지에 최근 본 상품 저장
    .then((res) => {
      if (!store.recent_jeonse == null) {
        const find_jeonse = store.recent_jeonse.find((depo) => depo.id == jeonse.value.id)
        if (store.recent_jeonse.length === 5) {
          if (!find_jeonse) {
            store.recent_jeonse.shift()
            store.recent_jeonse.push(jeonse.value)
          }
        } else {
          if (!find_jeonse) {
            store.recent_jeonse.push(jeonse.value)
          }
        }
      } else {
        store.recent_jeonse = [jeonse.value]
      }
    })
    //은행 정보
    .then((res)=>{
      // console.log(deposit.value)
      axios({
        method : 'get',
        url : `${store.API_URL}/info/bank/${jeonse.value.bank}/`
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
        url : `${store.API_URL}/info/user_join_jeonse/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
      })
      .then((res)=>{
        res.data.forEach((ele, idx) => {
          if (ele.id === jeonse.value.id) {
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
        url:`${store.API_URL}/info/jeonse_save/${jeonsePk}/`
      })
      .then((res)=>{
        recommended_products.value = res.data
      })
      .then((res) => {
        router.push({ name: 'jeonseDetail', params: { pk: jeonsePk } })
      })
    })
    .catch((err) => {
      console.log(err)
    })

}


//상품 저장 버튼
const productSave = function(event) {
  axios({
    method:'post',
    url: `${store.API_URL}/info/jeonse_save/${route.params.pk}/`,
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

const reload = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/jeonse/${route.params.pk}/`,
  })
  .then((res) => {
      console.log(res.data)
      jeonse.value = res.data
      opts.value = res.data.options
      option1.value = res.data.options[0]
    })
    // 로컬 스토리지에 최근 본 상품 저장
    .then((res) => {
      if (!store.recent_jeonse == null) {
        const find_jeonse = store.recent_jeonse.find((depo) => depo.id == jeonse.value.id)
        if (store.recent_jeonse.length === 5) {
          if (!find_jeonse) {
            store.recent_jeonse.shift()
            store.recent_jeonse.push(jeonse.value)
          }
        } else {
          if (!find_jeonse) {
            store.recent_jeonse.push(jeonse.value)
          }
        }
      } else {
        store.recent_jeonse = [jeonse.value]
      }
    })
    //은행 정보
    .then((res)=>{
      // console.log(deposit.value)
      axios({
        method : 'get',
        url : `${store.API_URL}/info/bank/${jeonse.value.bank}/`
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
        url : `${store.API_URL}/info/user_join_jeonse/`,
        headers: {
          Authorization: `Token ${store.token}`
        },
      })
      .then((res)=>{
        res.data.forEach((ele, idx) => {
          if (ele.id === jeonse.value.id) {
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
      url:`${store.API_URL}/info/jeonse_save/${route.params.pk}/`
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