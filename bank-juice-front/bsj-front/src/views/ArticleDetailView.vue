<template>
  <div v-if="article">
    <div class="container">
      <div>
        <p class="article-title">[공지] {{ article.title }}</p>
        <div class="top-text d-flex flex-row justify-content-between align-items-center">
          <p class="my-1">{{ formatDate(article.created_at) }} | 공지</p>
          <div>
            <button 
              class="btn" 
              @click="goUpdate"
              v-if="store.isStaff"
              >
              수정하기
            </button>
            <button 
              class="btn" 
              @click="goDelete"
              v-if="store.isStaff"
              >
              삭제하기
            </button>
          </div>
        </div>
        <hr>
        <div>
          <p class="bot-text">{{ article.content }}</p>
        </div>
        <hr>
        <button @click="goBack" class="btn back-btn shadow-sm">목록으로</button>
        <div class="mt-5">
          <p class="comment-top">댓글</p>
          <form 
            class="form-control" 
            @submit.prevent="createComment"
            v-if="store.isLogin"
          >
            <div class="d-flex flex-row justify-content-between">
              <input class="comment-input form-control" type="text" @input="inputComment" :value="content">
              <input class="btn" type="submit">
            </div>
          </form>
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
          <div v-if="article.comments">
            <div 
              v-for="(comment, index) in article.comments"
              :key="comment.id"
              @click="goDetail(comment.id)"
              class="mt-3 d-flex flex-column justify-content-around article-div"
            >
              <div class="top-text d-flex flex-row justify-content-between align-items-center">
                <span>{{ formatDate(comment.created_at) }}</span>
                <div v-if="store.isLogin">
                  <!-- <button 
                    class="btn" 
                    @click="goUpdateComment"
                    v-if="store.loginUser.username == comment.user.username"
                  >
                  수정
                  </button> -->
                  <button 
                    class="btn" 
                    @click="goDeleteComment(comment.id)"
                    v-if="store.loginUser.username == comment.user.username"
                  >
                  삭제
                  </button>
                </div>
              </div>
              <div class="mb-2">
                <span class="bot-text">{{ comment.content }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '../stores/counter';
import { ref, onMounted } from 'vue'

const route = useRoute()
const router = useRouter()
const articleId = route.params.id
const store = useCounterStore()

const article = ref(null)
const content = ref('')

const goBack = function() {
  router.go(-1)
}

const goUpdate = function () {
  router.push({ name: 'articleUpdate', params: { id: articleId }})
}

const goDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/communities/${articleId}/`,
    headers: {
            Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({name: 'community'})
    })
}

const goDeleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/communities/comment/${commentId}/`,
    headers: {
            Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    axios({
      method: 'get',
      url: `${store.API_URL}/communities/${articleId}/`,
      headers: {
              Authorization: `Token ${store.token}`
            },
    })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  })
}

const formatDate = function (date) {
  const currentDate = new Date(date)
  const year = currentDate.getFullYear()
  const month = String(currentDate.getMonth() + 1).padStart(2, '0')
  const day = String(currentDate.getDate()).padStart(2, '0')
  const hours = String(currentDate.getHours()).padStart(2, '0');
  const minutes = String(currentDate.getMinutes()).padStart(2, '0');
  const seconds = String(currentDate.getSeconds()).padStart(2, '0');
  return `${year}.${month}.${day} ${hours}:${minutes}:${seconds}`
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/communities/${articleId}/`,
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const inputComment = function (event) {
  content.value = event.currentTarget.value
  console.log(content)
}
const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/communities/${articleId}/comment/`,
    headers: {
            Authorization: `Token ${store.token}`
          },
    data: {
          content: content.value
    }
  })
    .then((res) => {
      content.value = ''
    })
    .then((res) => {
      axios({
        method: 'get',
        url: `${store.API_URL}/communities/${articleId}/`,
        headers: {
                Authorization: `Token ${store.token}`
              },
      })
        .then((res) => {
          article.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>
.comment-input {
  width: 90%;
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
.article-title {
  font-size: 30px;
}
.comment-top {
  color: gray;
  opacity: 0.8;
  font-size: 20px;
}
.back-btn {
  color: gray;
}
</style>