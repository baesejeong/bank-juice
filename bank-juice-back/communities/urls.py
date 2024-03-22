from django.urls import path
from . import views


app_name = "communities"
urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comment/', views.comment),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('article_search/<str:keyword>/', views.article_search),
]
