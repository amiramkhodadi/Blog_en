from account import views
from django.urls import path
# app_name = 'account'
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]