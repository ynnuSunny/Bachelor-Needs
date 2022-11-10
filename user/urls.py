from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name = "index"),
    path('login/',views.login,name="login"),
    path('signup/',views.goCreateAccount,name="signup"),
    path('home/',views.home,name="home"),
    path('createAccount/',views.createAccount,name="createAccount"),
    path('logout/',views.logout,name = "logout"),
    path('loginVarification/',views.loginVarification, name="loginVarification"),
    path('enterOtp/',views.goOtp, name="goOtp"),
    path('checkOtp/',views.checkOtp,name="checkOtp")
]