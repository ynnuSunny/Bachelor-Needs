from django.urls import path
from . import views

urlpatterns =[
 path('savePost/',views.savePost,name="savePost"),   
 path('shopHome/',views.shopHome,name="shopHome"),
 path('addComment/',views.addComment,name="addComment"),
 path('seeAllPost/',views.seeAllPost,name="seeAllPost"),
 
]