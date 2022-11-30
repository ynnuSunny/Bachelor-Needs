from django.urls import path
from . import views
from serviceProvider import views as spViews
from part_time_job import views as pjobviews

urlpatterns =[
    path('',views.main,name = "main"),
    path('index/',views.index,name = "index"),
    path('login/',views.login,name="login"),
    path('signup/',views.goCreateAccount,name="signup"),
    path('home/',views.home,name="home"),
    path('createAccount/',views.createAccount,name="createAccount"),
    path('logout/',views.logout,name = "logout"),
    path('loginVarification/',views.loginVarification, name="loginVarification"),
    path('enterOtp/',views.goOtp, name="goOtp"),
    path('checkOtp/',views.checkOtp,name="checkOtp"),
    path('createjob/',views.createjob,name = "createjob"),
    path('job_home/',pjobviews.job_home,name="job_home"),
    path('post_job/',views.post_job,name = "post_job")



]
