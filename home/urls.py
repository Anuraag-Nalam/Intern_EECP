from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('newp',views.newp,name="newp"),
    path('exip',views.exip,name="exip"),
    path('exipu',views.exipu,name="exipu"),
    path('after',views.after,name="after"),
    path('live',views.live,name='live')
]
