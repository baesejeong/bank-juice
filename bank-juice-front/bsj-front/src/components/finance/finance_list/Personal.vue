<template>
  <div>
    <div class="d-flex flex-column align-items-center mt-2 mb-5">
      <div class="form-div">
        <form class="form-control" @submit.prevent="searchProduct">
          <div class="d-flex flex-column align-items-center">
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="rateType">금리 유형</label>
              <select class="input-div mx-1 my-2 form-control" name="rateType" v-model="rateType" id="rateType">
                <option :value="1">기준금리</option>
                <option :value="2">가산금리</option>
                <option :value="3">가감조정금리</option>
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
              <label class="label-div mx-1" for="amount">대출액</label>
              <input class="input-div mx-1 my-2 form-control" name="amount" type="text" id="amount" v-model="amount">
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="creditScore">신용점수</label>
              <input class="input-div mx-1 my-2 form-control" type="text" id="creditScore" name="creditScore" v-model="creditScore">
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
            <th scope="col">월이자액</th>
            <th scope="col">이자율</th>
            <th scope="col">금리유형</th>
            <th scope="col">금융기관</th>
            <th scope="col">상품명</th>
          </tr>
        </thead>
        <tbody class="text-center">
          <tr 
            v-for="(personal, index) in personals"
            @click="goDetail(personal.personal)"
            class="product"
          >
            <th scope="row">{{ index + 1 }}</th>
            <td>
              <vue-number-format
                class="number-form text-center"
                :value="personal.loan_interest" 
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
            <td>{{ personal.rate }} %</td>
            <td>{{ personal.crdt_lend_rate_type_nm }}</td>
            <td>{{ personal.kor_co_nm }}</td>
            <td>{{ personal.fin_prdt_nm }}</td>
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
const personals = ref(null)

const rateType = ref(1)
const joinWay = ref('all')
const amount = ref(10000000)
const creditScore = ref(850)

const router = useRouter()


const searchProduct = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/personal/`,
    params: {
      rateType: rateType.value,
      joinWay: joinWay.value,
      amount: amount.value,
      creditScore: creditScore.value
    }
  })
    .then((res) => {
      console.log(res.data)
      personals.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/personal/`,
    params: {
      rateType: rateType.value,
      joinWay: joinWay.value,
      amount: amount.value,
      creditScore: creditScore.value
    }
  })
    .then((res) => {
      personals.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const goDetail = function (personalPk) {
  router.push({ name: 'personalDetail', params: { pk: personalPk } })
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
  width: 90%;
  margin-top: 20px;
}
.number-form {
  border: none;
}
th,td {
  white-space: nowrap;
}
</style>