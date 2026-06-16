from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.quiz_view, name="quiz"),
    path('user_view/',views.user_view, name="user_view"),
    path('submit/', views.quiz_submit_view, name='quiz_submit'),
    # path('career/result/<slug:career_slug>/',views.result_view, name="result_view"),

    path('result_view/',views.result_view, name="result_view"),
    path('score/',views.score_view, name="score_view"),
]
