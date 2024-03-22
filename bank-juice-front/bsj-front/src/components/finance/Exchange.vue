<template>
  <div> 
    <!-- 구글 환율 계산기가 매매기준율에 가까운 값으로 계산하므로 매매기준율로 계산하였다.  -->
    <!-- 매매기준율 : 여러 외화매매의 기준이 되는 환율로, 외환시장의 평균 환율을 의미 -->
    <!-- 출력할 데이터들을 걸러야할 것 -->
    <div class="container table-div d-flex flex-column align-items-center">
      <div class="shadow-sm top-table form-control my-4 d-flex flex-row justify-content-around align-items-center">
        <div class="d-flex flex-column cal-main-div">
          <h3 class="mb-4 text-center">환율 계산기</h3>
          <div>
            <!-- 국가 바꾸거나 무슨 값에서 무슨값으로 바꿀지 -->
            <div class="mb-2" v-if="from_data && to_data">
              1 {{ from_data.cur_nm }} =
              {{ exchange_rate }} {{ to_data.cur_nm}}
              <!-- 11월 20일 오후 3시 기준 -->
            </div>
            <div class="mt-3 me-3">
              <div class="my-2 cal-div d-flex flex-row justify-content-between">
                <input class="me-3 form-control" type="text" v-model="input_data" @input="calculate_exchange($event)">
                <select class="mx-2" v-model="from_data">
                  <option 
                    :value=data v-for="data in exchange_data" 
                    :key="data.id"
                  >
                    <span>{{ data.cur_nm }}({{ data.cur_unit }})</span>
                  </option>
                </select>
              </div>
              <div class="my-2 cal-div d-flex flex-row justify-content-between">
                <input class="me-3 form-control" type="text" v-model="result_data">
                <select class="mx-2" v-model="to_data">
                  <option 
                    :value=data v-for="data in exchange_data" 
                    :key="data.id"
                  >
                    <span>{{ data.cur_nm }}({{ data.cur_unit }})</span>
                  </option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <div>
          <table class="table shadow-sm">
            <thead class="text-center">
              <tr>
                <th scope="col">국가</th>
                <th class="red" scope="col">송금받을 때</th>
                <th class="blue" scope="col">송금보낼 때</th>
                <th scope="col">매매기준율</th>
              </tr>
            </thead>
            <tbody class="text-center">
              <tr v-if="usaData">
                <th><img class="country-img1" src="@/assets/usa.jpg" alt=""></th>
                <td class="red">{{ usaData.ttb }}</td>
                <td class="blue">{{ usaData.tts }}</td>
                <td>{{ usaData.deal_bas_r }}</td>
              </tr>
              
              <tr v-if="jpData">
                <th><img class="country-img2" src="@/assets/jp.jpg" alt=""></th>
                <td class="red">{{ jpData.ttb }}</td>
                <td class="blue">{{ jpData.tts }}</td>
                <td>{{ jpData.deal_bas_r }}</td>
              </tr>
              
              <tr v-if="euData">
                <th><img class="country-img3" src="@/assets/euro.jpg" alt=""></th>
                <td class="red">{{ euData.ttb }}</td>
                <td class="blue">{{ euData.tts }}</td>
                <td>{{ euData.deal_bas_r }}</td>
              </tr>

            </tbody>
          </table>
        </div>
      </div>

      <table class="table bot-table ">
        <thead class="text-center">
          <tr>
            <th scope="col">국가</th>
            <th class="red" scope="col">송금받을 때</th>
            <th class="blue" scope="col">송금보낼 때</th>
            <th scope="col">매매기준율</th>
          </tr>
        </thead>
        <tbody class="text-center">
          <tr 
            v-for="data in exchange_data" 
            :key="data.id"
            class=""
          >
            <th>{{ data.cur_nm }} ({{ data.cur_unit }})</th>
            <td class="red">{{ data.ttb }}</td>
            <td class="blue">{{ data.tts }}</td>
            <td>{{ data.deal_bas_r }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()
const from_data = ref(null)
const to_data = ref(null)
const input_data = ref(null)
const result_data = ref(null)
const jpData = ref(null)
const usaData = ref(null)
const euData = ref(null)

const exchange_rate = computed(()=>{
  const from_rate = parseFloat(from_data.value.deal_bas_r.replace(',',''))
  const to_rate = parseFloat(to_data.value.deal_bas_r.replace(',',''))
  result_data.value = input_data.value * Math.round((from_rate/to_rate)*100000)/100000
  return Math.round((from_rate / to_rate)*100000)/100000
})

const exchange_data = ref([])
onMounted(()=>{
  axios({
    method:'get',
    url:`${store.API_URL}/info/exchange/`
  })
  .then((res)=>{
    exchange_data.value = res.data
    from_data.value = res.data[13]
    to_data.value = res.data[22]
    exchange_data.value.forEach((exchange) => {
      if (exchange.cur_nm == '미국 달러') {
        usaData.value = exchange
      } else if (exchange.cur_nm == '일본 옌') {
        jpData.value = exchange
      } else if (exchange.cur_nm == '유로') {
        euData.value = exchange
      }
    })
  })
  .catch((err)=>{
    console.log(err)
  })
})

const calculate_exchange = function (event) {
  const from_rate = parseFloat(from_data.value.deal_bas_r.replace(',',''))
  const to_rate = parseFloat(to_data.value.deal_bas_r.replace(',',''))
  result_data.value = input_data.value * Math.round((from_rate/to_rate)*100000)/100000
}
</script>

<style scoped>
.top-table {
  width: 90%;
}
.table-div {
  width: 90%;
  margin-top: 100px;
}
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
.bot-table {
  width: 90%;
  margin-top: 20px;
}
.red {
  color: rgb(151, 5, 5);
}
.blue {
  color: rgb(66, 66, 232);
}
.country-img1{
  width: 45px;
}
.country-img2{
  width: 45px;
  border: 1px solid lightgray;
}
.country-img3{
  width: 45px;
}

</style>