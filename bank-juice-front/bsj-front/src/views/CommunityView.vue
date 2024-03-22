<template>
  <div>
    <div class="container mt-5">
      <div class="container mb-4 d-flex flex-row align-items-center justify-content-between">
        <p class="commu-title justify-content-center">공지사항</p>
        <RouterLink 
            :to="{ name: 'articleCreate' }"
            class="btn create-btn text-decoration-none justify-self-end"
            v-if="store.isStaff"
            >
            게시글 생성
        </RouterLink>
      </div>
      
      <ArticleList />
    </div>
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { RouterLink } from 'vue-router'
import { onMounted, ref } from 'vue'
import axios from 'axios';
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()

</script>

<style>
.commu-title {
  font-size: 30px;
  color: gray;
  opacity: 0.8;
}
.create-btn {
  background-color: #00C743 !important;
  color : white !important;
}

</style>
