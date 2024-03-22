<template>
  <div class="search-div">
    <div class="d-flex flex-column align-items-center">
      <div class="form-div mt-3 mb-5">
        <form @submit.prevent="searchKeyword" class="d-flex flex-row justify-content-center">
          <div class="search-input-div">
            <input class="ms-3 form-control search-input" type="text" v-model="keyword">
          </div>
          <div class="search-btn-div">
            <input class="ms-3 btn search-btn" type="submit" value="검색">
          </div>
        </form>
      </div>
      <div class="container">
        <div v-if="deposit_length">
          <p class="mt-5 mb-3 ms-5 product-title">예금</p>
          <div v-for="deposit in searched_data_deposit" class="d-flex flex-column align-items-center">
            <div class="card my-2 p-4 card-div">
              <div class="d-flex flex-row justify-content-between">
                <div class="d-flex flex-column justify-content-between">
                  <div>
                    <h2 class="mb-4">{{ deposit.fin_prdt_nm }}</h2>
                  </div>
                  <div>
                    <span class="my-3">{{ deposit.kor_co_nm }}</span>
                    <p class="my-2">가입 방법 : {{ deposit.join_way }}</p>
                  </div>
                </div>
                <div>
                  <div class="row gx-1" style="width: 300px;">
                    <div class="col pt-2">
                    <span>최고</span>
                    <div>
                      <span class=fs-4>
                        연 {{ searchOption(deposit).intr_rate2 }} %
                      </span>
                    </div>
                    </div>
                    <div class="col pt-2">
                      <span>기본</span>
                      <div>
                        <div>
                          <span class="fs-4">
                            연 {{ searchOption(deposit).intr_rate }} % 
                          </span>
                        </div>
                        <div class="mt-1 text-end">
                          <span style="color: gray">
                            ({{ searchOption(deposit).save_trm }}개월, 세전)
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex flex-row justify-content-end">
                    <button 
                      class="mt-3 btn form-btn"
                      @click="goDepositDetail(deposit.id)"
                    >
                      자세히 보러 가기
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr>
        </div>
        <div v-if="savings_length">
          <p class="mt-5 mb-3 ms-5 product-title">적금</p>
          <div v-for="savings in searched_data_savings" class="d-flex flex-column align-items-center">
            <div class="card my-2 p-4 card-div">
              <div class="d-flex flex-row justify-content-between">
                <div class="d-flex flex-column justify-content-between">
                  <div>
                    <h2 class="mb-4">{{ savings.fin_prdt_nm }}</h2>
                  </div>
                  <div>
                    <span class="my-3">{{ savings.kor_co_nm }}</span>
                    <p class="my-2">가입 방법 : {{ savings.join_way }}</p>
                  </div>
                </div>
                <div>
                  <div class="row gx-1" style="width: 300px;">
                    <div class="col pt-2">
                    <span>최고</span>
                    <div>
                      <span class=fs-4>
                        연 {{ searchOption(savings).intr_rate2 }} %
                      </span>
                    </div>
                    </div>
                    <div class="col pt-2">
                      <span>기본</span>
                      <div>
                        <div>
                          <span class="fs-4">
                            연 {{ searchOption(savings).intr_rate }} % 
                          </span>
                        </div>
                        <div class="mt-1 text-end">
                          <span style="color: gray">
                            ({{ searchOption(savings).save_trm }}개월, 세전)
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex flex-row justify-content-end">
                    <button 
                      class="mt-3 btn form-btn"
                      @click="goSavingsDetail(savings.id)"
                    >
                      자세히 보러 가기
                    </button>                  
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr>
        </div>
        <div v-if="personal_length">
          <p class="mt-5 mb-3 ms-5 product-title">신용 대출</p>
          <div v-for="personal in searched_data_personal" class="d-flex flex-column align-items-center">
            <div class="card my-2 p-4 card-div">
              <div class="d-flex flex-row justify-content-between">
                <div class="d-flex flex-column justify-content-between">
                  <div>
                    <h2 class="mb-4">{{ personal.fin_prdt_nm }}</h2>
                  </div>
                  <div>
                    <span class="my-3">{{ personal.kor_co_nm }}</span>
                    <p class="my-2">가입 방법 : {{ personal.join_way }}</p>
                  </div>
                </div>
                <div>
                  <div class="row gx-1" style="width: 300px;">
                    <div class="col pt-2">
                    <span>최고</span>
                    <div>
                      <span class=fs-4>
                        연 {{ personalOptionMax(personal) }} %
                      </span>
                    </div>
                    </div>
                    <div class="col pt-2">
                      <span>최저</span>
                      <div>
                        <div>
                          <span class="fs-4">
                            연 {{ personalOptionMin(personal) }} % 
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="mt-1 text-end">
                    <span style="color: gray">
                      ({{ selectOption(personal).crdt_lend_rate_type_nm }} 기준)
                    </span>
                  </div>
                  <div class="d-flex flex-row justify-content-end">
                    <button 
                      class="mt-3 btn form-btn"
                      @click="goPersonalDetail(personal.id)"
                    >
                      자세히 보러 가기
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr>
        </div>
        <div v-if="mortgage_length">
          <p class="mt-5 mb-3 ms-5 product-title">주택 담보 대출</p>
          <div v-for="mortgage in searched_data_mortgage" class="d-flex flex-column align-items-center">
            <div class="card my-2 p-4 card-div">
              <div class="d-flex flex-row justify-content-between">
                <div class="d-flex flex-column justify-content-between">
                  <div>
                    <h2 class="mb-4">{{ mortgage.fin_prdt_nm }}</h2>
                  </div>
                  <div>
                    <span class="my-3">{{ mortgage.kor_co_nm }}</span>
                    <p class="my-2">가입 방법 : {{ mortgage.join_way }}</p>
                  </div>
                </div>
                <div>
                  <div class="row gx-1" style="width: 300px;">
                    <div class="col pt-2">
                    <span>최고</span>
                    <div>
                      <span class=fs-4>
                        연 {{ selectOption(mortgage).lend_rate_max }} %
                      </span>
                    </div>
                    </div>
                    <div class="col pt-2">
                      <span>최저</span>
                      <div>
                        <div>
                          <span class="fs-4">
                            연 {{ selectOption(mortgage).lend_rate_min }} % 
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="mt-1 text-end">
                    <span style="color: gray">
                      ({{ selectOption(mortgage).mrtg_type_nm }}, {{ selectOption(mortgage).rpay_type_nm }}, {{ selectOption(mortgage).lend_rate_type_nm }} 기준)
                    </span>
                  </div>
                  <div class="d-flex flex-row justify-content-end">
                    <button 
                      class="mt-3 btn form-btn"
                      @click="goMortgageDetail(mortgage.id)"
                    >
                      자세히 보러 가기
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr>
        </div>
        <div v-if="jeonse_length">
          <p class="mt-5 mb-3 ms-5 product-title">전세 대출</p>
          <div v-for="jeonse in searched_data_jeonse" class="d-flex flex-column align-items-center">
            <div class="card my-2 p-4 card-div">
              <div class="d-flex flex-row justify-content-between">
                <div class="d-flex flex-column justify-content-between">
                  <div>
                    <h2 class="mb-4">{{ jeonse.fin_prdt_nm }}</h2>
                  </div>
                  <div>
                    <span class="my-3">{{ jeonse.kor_co_nm }}</span>
                    <p class="my-2">가입 방법 : {{ jeonse.join_way }}</p>
                  </div>
                </div>
                <div>
                  <div class="row gx-1" style="width: 300px;">
                    <div class="col pt-2">
                    <span>최고</span>
                    <div>
                      <span class=fs-4>
                        연 {{ selectOption(jeonse).lend_rate_max }} %
                      </span>
                    </div>
                    </div>
                    <div class="col pt-2">
                      <span>최저</span>
                      <div>
                        <div>
                          <span class="fs-4">
                            연 {{ selectOption(jeonse).lend_rate_min }} % 
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="mt-1 text-end">
                    <span style="color: gray">
                      ({{ selectOption(jeonse).rpay_type_nm }}, {{ selectOption(jeonse).lend_rate_type_nm }} 기준)
                    </span>
                  </div>
                  <div class="d-flex flex-row justify-content-end">
                    <button 
                      class="mt-3 btn form-btn"
                      @click="goJeonseDetail(jeonse.id)"
                    >
                      자세히 보러 가기
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <hr>
        </div>
        <div v-if="article_length" class="d-flex flex-column align-items-center">
          <h2>공지 사항</h2>
          {{ searched_data_article }}
          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const keyword = ref(null)
const store = useCounterStore()
const router = useRouter()

const searched_data_deposit = ref(null)
const deposit_length = ref(null)
const searched_data_savings = ref(null)
const savings_length = ref(null)
const searched_data_personal = ref(null)
const personal_length = ref(null)
const searched_data_mortgage = ref(null)
const mortgage_length = ref(null)
const searched_data_jeonse = ref(null)
const jeonse_length = ref(null)
const searched_data_article = ref(null)
const article_length = ref(null)

const goDepositDetail = function (depositPk) {
  router.push({ name: 'depositDetail', params: { pk: depositPk } })
}

const goSavingsDetail = function (savingsPk) {
  router.push({ name: 'savingsDetail', params: { pk: savingsPk } })
}

const goPersonalDetail = function (personalPk) {
  router.push({ name: 'personalDetail', params: { pk: personalPk } })
}

const goMortgageDetail = function (mortgagePk) {
  router.push({ name: 'mortgageDetail', params: { pk: mortgagePk } })
}

const goJeonseDetail = function (jeonsePk) {
  router.push({ name: 'jeonseDetail', params: { pk: jeonsePk } })
}

const searchOption = function (product) {
  const options= product.options
  const option_6 = options.filter((option) => option.save_trm == 6)[0]
  const option_12 = options.filter((option) => option.save_trm == 12)[0]
  const option_24 = options.filter((option) => option.save_trm == 24)[0]
  const option_36 = options.filter((option) => option.save_trm == 36)[0]
  
  if (option_12) {
    return option_12
  } else if (option_6) {
    return option_6
  } else if (option_24) {
    return option_24
  } else if (option_36) {
    return option_36
  }
}

const personalOptionMin = function (product) {
  const option= product.options[0]
  const option_1 = option.crdt_grad_1
  const option_4 = option.crdt_grad_4
  const option_5 = option.crdt_grad_5
  const option_6 = option.crdt_grad_6
  const option_10 = option.crdt_grad_10
  const option_11 = option.crdt_grad_11
  const option_12 = option.crdt_grad_12
  const option_13 = option.crdt_grad_13
  
  if (option_1) {
    return option_1
  } else if (option_4) {
    return option_4
  } else if (option_5) {
    return option_5
  } else if (option_6) {
    return option_6
  } else if (option_10) {
    return option_10
  } else if (option_11) {
    return option_11
  } else if (option_12) {
    return option_12
  } else if (option_13) {
    return option_13
  }
}

const personalOptionMax = function (product) {
  const option= product.options[0]
  const option_1 = option.crdt_grad_1
  const option_4 = option.crdt_grad_4
  const option_5 = option.crdt_grad_5
  const option_6 = option.crdt_grad_6
  const option_10 = option.crdt_grad_10
  const option_11 = option.crdt_grad_11
  const option_12 = option.crdt_grad_12
  const option_13 = option.crdt_grad_13
  
  if (option_13) {
    return option_13
  } else if (option_12) {
    return option_12
  } else if (option_11) {
    return option_11
  } else if (option_10) {
    return option_10
  } else if (option_6) {
    return option_6
  } else if (option_5) {
    return option_5
  } else if (option_4) {
    return option_4
  } else if (option_1) {
    return option_1
  }
}


const selectOption = function (product) {
  return product.options[0]
}

const searchKeyword = function () {
  axios({
    method:'get',
    url: `${store.API_URL}/search/deposit_search/${keyword.value}/`,
  })
    .then((res)=>{
      console.log(res.data)
      searched_data_deposit.value = res.data
      deposit_length.value = res.data.length

    })
    .catch((err)=>{
      console.log(1)
      console.log(err)
    })
  axios({
    method:'get',
    url: `${store.API_URL}/search/savings_search/${keyword.value}/`,
  })
  .then((res)=>{
      searched_data_savings.value = res.data
      savings_length.value = res.data.length

    })
    .catch((err)=>{
      console.log(err)
    })
    axios({
    method:'get',
    url: `${store.API_URL}/search/personal_search/${keyword.value}/`,
  })
  .then((res)=>{
      searched_data_personal.value = res.data
      personal_length.value = res.data.length
      
    })
    .catch((err)=>{
      console.log(err)
    })
    axios({
    method:'get',
    url: `${store.API_URL}/search/mortgage_search/${keyword.value}/`,
  })
  .then((res)=>{
      searched_data_mortgage.value = res.data
      mortgage_length.value = res.data.length
    })
    .catch((err)=>{
      console.log(err)
    })
    axios({
    method:'get',
    url: `${store.API_URL}/search/jeonse_search/${keyword.value}/`,
  })
  .then((res)=>{
      searched_data_jeonse.value = res.data
      jeonse_length.value = res.data.length
    })
    .catch((err)=>{
      console.log(err)
    })
   
  axios({
    method:'get',
    url: `${store.API_URL}/communities/article_search/${keyword.value}/`,
  })
    .then((res)=>{
      searched_data_article.value = res.data
      article_length.value = res.data.length
    })
    .catch((err)=>{
      console.log(err)
    })
}

</script>

<style scoped>
.form-div {
  width: 70%;
}
.search-btn {
  background-color: #00C743;
  color : white;
}
.form-btn {
  background-color: #b2ecc5;
  color: #02b03c;
  width: 100%;
}
.card-div {
  width: 90%;
}
.product-title {
  font-size: 25px;
  margin-left: 10px;
  color: gray;
  font-family: NanumSquareNeoExtraBold;
  opacity: 0.8;
}
input[type=text]{
  height: 50px;
  font-size: 25px;
  padding-left: 25px;
  border-radius: 40px;
}
input[type=submit]{
  height: 50px;
  font-size: 20px;
}
.search-input {
  width: 100%;
}
.search-input-div {
  margin-left: 15%;
  margin-right: 2rem;
  width: 60%;
}
.search-btn-div {
  width: 20%;
}
</style>