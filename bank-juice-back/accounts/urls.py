from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('update/', views.profile_update),
    path('user_info/', views.user_info),
    path('user_staff/', views.user_staff),
]
