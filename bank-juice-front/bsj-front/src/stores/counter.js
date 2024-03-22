import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const route = useRoute()
  const articles = ref([])
  // const API_URL = 'http://3.38.107.181:8000/'
  const API_URL = 'http://127.0.0.1:8000'

  const token = ref(null)

  const my_deposits = ref(null)
  const my_savingss = ref(null)
  const my_personals = ref(null)
  const my_mortgages = ref(null)
  const my_jeonses = ref(null)

  const recent_deposit = ref([])
  const recent_savings = ref([])
  const recent_personal = ref([])
  const recent_mortgage = ref([])
  const recent_jeonse = ref([])
  const loginUser = ref(null)
  const isStaff = ref(false)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        if (username.length == 0) {
          Swal.fire({
            title: 'Error!',
            text: '아이디를 입력해 주세요!',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          })
        } else if (username.length < 5) {
          Swal.fire({
            title: 'Error!',
            text: '아이디의 길이를 확인해 주세요.',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          }) 
        } else if (username.length > 15) {
          Swal.fire({
            title: 'Error!',
            text: '아이디의 길이를 확인해 주세요.',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          }) 
        } else if (password1.length == 0) {
          Swal.fire({
            title: 'Error!',
            text: '비밀번호를 입력해 주세요!',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          })
        } else if (password1.length < 8) {
          Swal.fire({
            title: 'Error!',
            text: '사용 불가능한 비밀번호입니다.',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          })
        } else if (password1.length > 16) {
          Swal.fire({
            title: 'Error!',
            text: '사용 불가능한 비밀번호입니다.',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          })
        } else if (password1 != password2) {
          Swal.fire({
            title: 'Error!',
            text: '비밀번호가 일치하지 않습니다.',
            icon: 'error',
            showCancelButton: false,
            confirmButtonColor: '#d33',
            confirmButtonText: '닫기',
          })
        }
        console.log(username.length)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
      })
      .catch((err) => {
        Swal.fire({
          title: 'Error!',
          text: '로그인 정보가 올바르지 않습니다.',
          icon: 'error',
          showCancelButton: false,
          confirmButtonColor: '#d33',
          confirmButtonText: '닫기',
        }) 
      })
      .then((res)=> {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user_staff/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
        .then((res) => {
          if (res.data == 'True') {
            isStaff.value = true
          } else {
            isStaff.value = false
          }
        })
      })
      .then((res) => {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user_info/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
        .then((res) => {
          loginUser.value = res.data
          if (loginUser.value.nickname === null) {
            router.push({ name: 'addProfile' })
          } else {
            router.push({ name: 'main' })
          }
        })
        .catch((err) => {
          console.log(err)
        })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        recent_deposit.value = null
        recent_savings.value = null
        recent_personal.value = null
        recent_mortgage.value = null
        recent_jeonse.value = null
        loginUser.value = null
        isStaff.value = false
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const addProfileData = function (payload) {
    const { nickname, email, age, gender, salary } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/update/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        nickname, email, age, gender, salary
      }
    })
      .then((res) => {
        console.log(res.data)
        loginUser.value = res.data
        router.push({ name : 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const recommend_user_deposits = ref([])
  const recommend_user_savings = ref([])
  const recommend_user_personals = ref([])
  const recommend_user_mortgages = ref([])
  const recommend_user_jeonses = ref([])
  
  const recommended_deposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/info/user_recommend_deposit/`,
      headers: {
            Authorization: `Token ${token.value}`
          }
    })
      .then((res) => {
        recommend_user_deposits.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const recommended_savings = function () {
    axios({
      method: 'get',
      url: `${API_URL}/info/user_recommend_savings/`,
      headers: {
            Authorization: `Token ${token.value}`
          }
    })
      .then((res) => {
        recommend_user_savings.value= res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  const recommended_personal = function () {
    axios({
      method: 'get',
      url: `${API_URL}/info/user_recommend_personal/`,
      headers: {
            Authorization: `Token ${token.value}`
          }
    })
      .then((res) => {
        recommend_user_personals.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const recommended_jeonse = function () {
    axios({
      method: 'get',
      url: `${API_URL}/info/user_recommend_jeonse/`,
      headers: {
            Authorization: `Token ${token.value}`
          }
    })
      .then((res) => {
        recommend_user_jeonses.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const recommended_mortgage = function () {
    axios({
      method: 'get',
      url: `${API_URL}/info/user_recommend_mortgage/`,
      headers: {
            Authorization: `Token ${token.value}`
          }
    })
      .then((res) => {
        recommend_user_mortgages.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { 
    articles, API_URL, loginUser, isStaff,
    recent_deposit, recent_savings, recent_personal, recent_mortgage, recent_jeonse,
    signUp, logIn, token, isLogin, logOut, addProfileData, 
    my_deposits, my_savingss, my_personals, my_mortgages, my_jeonses,
    recommended_deposit, recommended_savings, recommended_jeonse, 
    recommended_mortgage, recommended_personal,
    recommend_user_deposits, recommend_user_savings,
    recommend_user_personals, recommend_user_jeonses, recommend_user_mortgages
  }
}, { persist: true })

