from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('career_chat/', views.career_chat_ai,name="career_chat_ai"),
    path('logout/',views.user_logout,name='logout'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
]