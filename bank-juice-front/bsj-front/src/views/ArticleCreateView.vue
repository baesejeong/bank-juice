<template>
  <div class="my-5">
    <div class="d-flex flex-column align-items-center">
      <div class="form-div ">
        <p class="create-title my-4 align-self-start ">게시글 작성</p>
      </div>
      <form 
        @submit.prevent="createArticle"
        class="form-div form-control d-flex flex-column shadow-sm"
      >
        <div class="d-flex flex-column mb-3">
          <label class="mt-3 mb-1 label-div" for="title">제목</label>
          <input 
            class="form-control input-div shadow-sm" 
            id="title" 
            type="text"
            v-model.trim="title"
            placeholder="제목을 입력해주세요."
          >      
        </div>

        <div class="d-flex flex-column mb-3">
          <label class="mt-3 mb-1 label-div" for="content">내용</label>
          <textarea 
            name="" id="content" 
            class="form-control textarea-div py-3 shadow-sm"
            v-model.trim="content"
            placeholder="내용을 입력해주세요."
          >
          </textarea>
        </div>
        
        <input class="mt-3 mb-2 btn form-btn shadow-sm" type="submit" value="게시글 생성">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/communities/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'community' })
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>
<style scoped>
.create-title {
  font-size: 25px;
  margin-left: 10px;
  color: gray;
  font-family: NanumSquareNeoExtraBold;
  opacity: 0.8;
}
.form-div {
  width: 70%;
}
.label-div {
  font-family: 'NanumSquareNeoBold';
  color: black;
  opacity: 0.8;
  font-size: 20px;
  margin-left: 90px;
}
.input-div {
  align-self: center;
  height: 50px;
  width: 80%;
  font-size: 17px;
  padding-left: 25px;
  border-radius: 10px;
}
.textarea-div {
  align-self: center;
  height: 500px;
  width: 80%;
  font-size: 17px;
  padding-left: 25px;
  border-radius: 10px;
}
.form-btn {
  align-self: center;
  height: 45px;
  width: 70%;
  font-size: 20px;
  background-color: #b2ecc5;
  color: #02b03c;
}
</style>