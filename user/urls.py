from django.urls import path
from . import views
from serviceProvider import views as spViews

urlpatterns =[
    path('',views.main,name = "main"),
    path('index/',views.index,name = "user-index"),
    path('login/',views.login,name="user-login"),
    path('signup/',views.signup,name="user-signup"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name = "user-logout"),
    path('userVarification/',views.userVarification, name="userVarification"),

    
]