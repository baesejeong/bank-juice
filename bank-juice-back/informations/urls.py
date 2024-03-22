from django.urls import path
from . import views

app_name = "informations"
urlpatterns = [
    path('bank/', views.bank),
    path('bank/<int:bank_pk>/', views.bank_detail),
    
    path('exchange/', views.exchange),
    
    path('deposit/', views.deposit),
    path('deposit/<int:deposit_pk>/', views.deposit_detail),
    path('deposit_save/<int:deposit_pk>/', views.deposit_save),

    path('savings/', views.savings),
    path('savings/<int:savings_pk>/', views.savings_detail),
    path('savings_save/<int:savings_pk>/', views.savings_save),

    path('personal/', views.personal),
    path('personal/<int:personal_pk>/', views.personal_detail),
    path('personal_save/<int:personal_pk>/', views.personal_save),

    path('mortgage/', views.mortgage),
    path('mortgage/<int:mortgage_pk>/', views.mortgage_detail),
    path('mortgage_save/<int:mortgage_pk>/', views.mortgage_save),

    path('jeonse/', views.jeonse),
    path('jeonse/<int:jeonse_pk>/', views.jeonse_detail),
    path('jeonse_save/<int:jeonse_pk>/', views.jeonse_save),

    # 로그인 한 사용자와 유사한 유저들의 데이터를 응답
    path('user_recommend_deposit/', views.user_recommend_deposit),
    path('user_recommend_savings/', views.user_recommend_savings),
    path('user_recommend_personal/', views.user_recommend_personal),
    path('user_recommend_mortgage/', views.user_recommend_mortgage),
    path('user_recommend_jeonse/', views.user_recommend_jeonse),

    # 상품 타입 별 검색 결과 응답
    path('deposit_search/<str:keyword>/', views.deposit_search),
    path('savings_search/<str:keyword>/', views.savings_search),
    path('personal_search/<str:keyword>/', views.personal_search),
    path('mortgage_search/<str:keyword>/', views.mortgage_search),
    path('jeonse_search/<str:keyword>/', views.jeonse_search),

    # 로그인 한 사용자가 가입한 상품 응답
    path('user_join_deposit/', views.user_join_deposit),
    path('user_join_savings/', views.user_join_savings),
    path('user_join_personal/', views.user_join_personal),
    path('user_join_mortgage/', views.user_join_mortgage),
    path('user_join_jeonse/', views.user_join_jeonse),
]
