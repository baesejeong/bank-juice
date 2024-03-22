<template>
  <div class="container">
    <div class="list-div">
      <div v-if="articles.length > 0" class="container">
        <div
          v-for="(article, index) in articles"
          :key="article.id"
          @click="goDetail(article.id)"
          class="d-flex flex-column justify-content-around article-div"
        >
          <div>
            <span class="top-text">{{ formatDate(article.created_at) }} | 공지</span>
          </div>
          <div class="mb-2">
            <span class="bot-text">[공지] {{ article.title }}</span>
          </div>
        </div>
      </div>
    <div v-else>
      <h2>아직 공지사항이 없습니다.</h2>
    </div>
  </div>
    
    
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const articles = ref([])
const store = useCounterStore()
const router = useRouter()

const goDetail = function (articlePk) {
  router.push({ name: 'articleDetail', params: { id: articlePk }})
}

const formatDate = function (date) {
  const currentDate = new Date(date)
  const year = currentDate.getFullYear()
  const month = String(currentDate.getMonth() + 1).padStart(2, '0')
  const day = String(currentDate.getDate()).padStart(2, '0')
  return `${year}.${month}.${day}`
}

onMounted(() => {
    // DRF에 article 조회 요청을 보내는 action
    axios({
      method: 'get',
      url: `${store.API_URL}/communities/`,
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
})
</script>

<style scoped>
.card-div {
  height: 50px;
  display: flex;
  flex-direction: row;
  align-items: center;
  font-size: 20px;
  padding-left: 20px;
  font-family: 'NanumSquareNeoExtraBold';
}
.list-div {
  border-top: 2px solid black;
}
.article-div {
  height: 100px;
  border-bottom: 1px solid lightgray;
}
.top-text {
  color: gray;
  opacity: 0.8;
  font-size: 15px;
}
.bot-text {
  font-size: 20px;
}
</style>