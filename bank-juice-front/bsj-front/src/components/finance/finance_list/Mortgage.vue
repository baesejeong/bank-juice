<template>
  <div>
    <div class="d-flex flex-column align-items-center mt-2 mb-5">
      <div class="form-div">
        <form class="form-control" @submit.prevent="searchProduct">
          <div class="d-flex flex-column align-items-center">
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="houseType">주택종류</label>
              <select class="input-div mx-1 my-2 form-control" name="houseType" v-model="houseType" id="houseType">
                <option :value="'1'">아파트</option>
                <option :value="'2'">아파트 외</option>        
              </select>
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="joinWay">가입 방식</label>
              <select class="input-div mx-1 my-2 form-control" name="joinWay" v-model="joinWay" id="joinWay">
                <option :value="'all'">전체</option>
                <option :value="'online'">온라인</option>
                <option :value="'visit'">방문</option>
              </select>
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="repayWay">상환 방식</label>
              <select class="input-div mx-1 my-2 form-control" name="repayWay" v-model="repayWay" id="repayWay">
                <option :value="'1'">분할상환방식</option>
                <option :value="'2'">만기일시상환방식</option>
              </select>
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="rateType">금리 방식</label>
              <select class="input-div mx-1 my-2 form-control" name="rateType" v-model="rateType" id="rateType">
                <option :value="'1'">고정금리</option>
                <option :value="'2'">변동금리</option>        
              </select>
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="amount">대출액</label>
              <input class="input-div mx-1 my-2 form-control" name="amount" type="text" id="amount" v-model="amount">      
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="period">기간</label>
              <input class="input-div mx-1 my-2 form-control" type="text" id="period" name="period" v-model="period">      
            </div>

            <div class="my-3">
              <input class="btn form-btn" type="submit" value="계산하기">
            </div>
          </div>
        </form>
      </div>
      <table class="table">
        <thead class="text-center">
          <tr>
            <th scope="col">번호</th>
            <th scope="col">최저금리</th>
            <th scope="col">월최저상환액</th>
            <th scope="col">최대금리</th>
            <th scope="col">월최대상환액</th>
            <th scope="col">상품명</th>
            <th scope="col">금융기관</th>
            <th scope="col">금리유형</th>
            <th scope="col">주택유형</th>
            <th scope="col">담보유형</th>
          </tr>
        </thead>
        <tbody class="text-center">
          <tr 
            v-for="(mortgage, index) in mortgages"
            @click="goDetail(mortgage.mortgage)"
            class="product"
          >
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ mortgage.lend_rate_min }}</td>
            <td>
              <vue-number-format
                class="number-form text-center"
                :value="mortgage.loan_interest_min" 
                :options="{ 
                  thousand: ',',
                  decimal: '.',
                  prefix: '',
                  precision: 0,
                  suffix: ' 원',
                  }"
              >
              </vue-number-format>
            </td>
            <td>{{ mortgage.lend_rate_max }}</td>
            <td>
              <vue-number-format
                class="number-form text-center"
                :value="mortgage.loan_interest_max" 
                :options="{ 
                  thousand: ',',
                  decimal: '.',
                  prefix: '',
                  precision: 0,
                  suffix: ' 원',
                  }"
              >
              </vue-number-format>
            </td>
            <td>{{ mortgage.fin_prdt_nm }}</td>
            <td>{{ mortgage.kor_co_nm }}</td>
            <td>{{ mortgage.lend_rate_type_nm }}</td>
            <td>{{ mortgage.mrtg_type_nm }}</td>
            <td>{{ mortgage.rpay_type_nm }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useCounterStore } from '../../../stores/counter';
import { useRouter } from 'vue-router';
import VueNumberFormat from 'vue-number-format'
const store = useCounterStore()
const mortgages = ref(null)

const houseType = ref('1')
const joinWay = ref('all')
const repayWay = ref('1')
const rateType = ref('1')

const amount = ref(10000000)
const period = ref(2)

const router = useRouter()


const searchProduct = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/mortgage/`,
    params: {
      houseType: houseType.value,
      joinWay: joinWay.value,
      repayWay: repayWay.value,
      rateType: rateType.value,
      amount: amount.value,
      period : period.value,
    }
  })
    .then((res) => {
      console.log(res.data)
      mortgages.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/mortgage/`,
    params: {
      houseType: houseType.value,
      joinWay: joinWay.value,
      repayWay: repayWay.value,
      rateType: rateType.value,
      amount: amount.value,
      period : period.value,
    }
  })
    .then((res) => {
      mortgages.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const goDetail = function (mortgagePk) {
  console.log(mortgagePk)
  router.push({ name: 'mortgageDetail', params: { pk: mortgagePk } })
}

</script>

<style  scoped>
.form-div {
  width: 60%;
}
.form-input-div {
  width: 90%;
}
.label-div {
  width: 10%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-size: 16px;
}
.input-div {
  width: 80%;
}
.form-btn {
  background-color: #00C743 !important;
  color : white !important;
  width: 150%;
}
thead {
  border-bottom: 3px double lightgray;
}
table {
  width: 100%;
  margin-top: 20px;
}
.number-form {
  border: none;
}
th,td {
  white-space: nowrap;
}
</style>