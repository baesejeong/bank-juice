<template>
  <div>
    <div class="d-flex flex-column align-items-center mt-2 mb-5">
      <div class="form-div">
        <form class="form-control" @submit.prevent="searchProduct">
          <div class="d-flex flex-column align-items-center">
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="tariff">세율</label>
              <select class="input-div mx-1 my-2 form-control" name="tariff" v-model="tariff" id="tariff">
                <option :value="0.154">일반과세</option>
                <option :value="0.014">세금우대</option>
                <option :value="0">비과세</option>
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
              <label class="label-div mx-1" for="amount">예치금액</label>
              <input class="input-div mx-1 my-2 form-control" name="amount" type="text" id="amount" v-model="amount">
            </div>
            
            <div class="form-input-div d-flex flex-row justify-content-around">
              <label class="label-div mx-1" for="period">예치기간</label>
              <select class="input-div mx-1 my-2 form-control" name="period" v-model="period" id="period">
                <option :value="6">6개월</option>
                <option :value="12">12개월</option>
                <option :value="24">24개월</option>
                <option :value="36">36개월</option>
              </select>
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
            <th scope="col">순위</th>
            <th scope="col">6개월</th>
            <th scope="col">12개월</th>
            <th scope="col">세전이자</th>
            <th scope="col">세후이자</th>
            <th scope="col">24개월</th>
            <th scope="col">36개월</th>
            <th scope="col">금융기관</th>
            <th scope="col">상품명</th>
          </tr>
        </thead>
        <tbody class="text-center">
          <tr 
            v-for="(save, index) in savings"
            @click="goDetail(save.savings)"
            class="product"
          >
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ save.intr_rate_6 ? save.intr_rate_6 : '-' }}</td>
            <td>{{ save.intr_rate_12 ? save.intr_rate_12 : '-' }}</td>
            <td>
              <vue-number-format
                class="number-form text-center"
                :value="save.interest_before_tax" 
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
            <td>
              <vue-number-format
                class="number-form text-center"
                :value="save.interest_after_tax" 
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
            <td>{{ save.intr_rate_24 ? save.intr_rate_24 : '-' }}</td>
            <td>{{ save.intr_rate_36 ? save.intr_rate_36 : '-' }}</td>
            <td>{{ save.kor_co_nm }}</td>
            <td>{{ save.fin_prdt_nm }}</td>
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
const savings = ref(null)

const tariff = ref(0.154)
const joinWay = ref('all')
const amount = ref(10000000)
const period = ref(12)

const router = useRouter()


const searchProduct = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/savings/`,
    params: {
      tariff: tariff.value,
      joinWay: joinWay.value,
      amount: amount.value,
      period: period.value
    }
  })
    .then((res) => {
      console.log(res.data)
      savings.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/info/savings/`,
    params: {
      tariff: tariff.value,
      joinWay: joinWay.value,
      amount: amount.value,
      period: period.value
    }
  })
    .then((res) => {
      savings.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const goDetail = function (savingsPk) {
  router.push({ name: 'savingsDetail', params: { pk: savingsPk } })
}

</script>

<style  scoped>.form-div {
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