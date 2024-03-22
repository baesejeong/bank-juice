import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'

import FinanceView from '@/views/FinanceView.vue'

import Finance from '@/components/finance/Finance.vue'
import Deposit from '@/components/finance/finance_list/Deposit.vue'
import Savings from '@/components/finance/finance_list/Savings.vue'

import Loan from '@/components/finance/Loan.vue'
import Personal from '@/components/finance/finance_list/Personal.vue'
import Mortgage from '@/components/finance/finance_list/Mortgage.vue'
import Jeonse from '@/components/finance/finance_list/Jeonse.vue'

import Exchange from '@/components/finance/Exchange.vue'

import CommunityView from '@/views/CommunityView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import SignupDetailView from '@/views/SignupDetailView.vue'

import ArticleDetailView from '@/views/ArticleDetailView.vue'

import DepositDetailView from '@/views/finance_detail/DepositDetailView.vue'
import SavingsDetailView from '@/views/finance_detail/SavingsDetailView.vue'
import PersonalDetailView from '@/views/finance_detail/PersonalDetailView.vue'
import MortgageDetailView from '@/views/finance_detail/MortgageDetailView.vue'
import JeonseDetailView from '@/views/finance_detail/JeonseDetailView.vue'

import ProfileView from '@/views/ProfileView.vue'
import ProfileJoin from '@/components/profile/ProfileJoin.vue'
import ProfileRecommend from '@/components/profile/ProfileRecommend.vue'
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/finance',
      name: 'finance',
      component: FinanceView,
      children: [
        {
          path: '',
          name: 'bank',
          component: Finance,
          children: [
            {
              path: '',
              name: 'deposit',
              component: Deposit
            },
            {
              path: 'savings',
              name: 'savings',
              component: Savings
            },
          ]
        },
        {
          path: 'loan',
          name: 'loan',
          component: Loan,
          children: [
            {
              path: '',
              name: 'personal',
              component: Personal
            },
            {
              path: 'mortgage',
              name: 'mortgage',
              component: Mortgage
            },
            {
              path: 'jeonse',
              name: 'jeonse',
              component: Jeonse
            },
          ]
        },
        {
          path: 'exchange',
          name: 'exchange',
          component: Exchange
        },
      ]
    },
    {
      path: '/depositDetail/:pk',
      name: 'depositDetail',
      component: DepositDetailView
    },
    {
      path: '/savingsDetail/:pk',
      name: 'savingsDetail',
      component: SavingsDetailView
    },
    {
      path: '/personalDetail/:pk',
      name: 'personalDetail',
      component: PersonalDetailView
    },
    {
      path: '/mortgageDetail/:pk',
      name: 'mortgageDetail',
      component: MortgageDetailView
    },
    {
      path: '/jeonseDetail/:pk',
      name: 'jeonseDetail',
      component: JeonseDetailView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      children: [
        {
          path: '',
          name: 'myjoin',
          component: ProfileJoin
        },   
        {
          path: 'myrecommend',
          name: 'myrecommend',
          component: ProfileRecommend
        },   
        {
          path: 'myupdate',
          name: 'myupdate',
          component: ProfileUpdate
        },
      ]
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/create',
      name: 'articleCreate',
      component: ArticleCreateView
    },
    {
      path: '/article/:id',
      name: 'articleDetail',
      component: ArticleDetailView
    },
    {
      path: '/article/update/:id',
      name: 'articleUpdate',
      component: ArticleUpdateView
    },

    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/addProfile',
      name: 'addProfile',
      component: SignupDetailView
    },
  ]
})

export default router
