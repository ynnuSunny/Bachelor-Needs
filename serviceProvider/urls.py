from django.urls import path
from . import views

urlpatterns =[
    
   path('goSpLogin/',views.goSpLogin,name="goSpLogin"),
   path('goSpSingup/',views.goSpSingup,name="goSpSingup"),
   path('enterOtp/',views.goOtp, name="goOtp"),
   path('signUp/',views.signUp,name="signUp2"),
   path('checkOtp2/',views.checkOtp2,name="checkOtp2")
    # path('signup/',views.goCreateAccount,name="signup"),
    # path('registration/',views.registration,name="registration"),
    # path('createAccount/',views.createAccount,name="createAccount"),
    # path('logout/',views.logout,name = "logout"),
    # path('loginVarification/',views.loginVarification, name="loginVarification"),
    # path('enterOtp/',views.goOtp, name="goOtp"),
    # path('checkOtp/',views.checkOtp,name="checkOtp")
]