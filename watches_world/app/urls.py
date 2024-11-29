from django.urls import path
from . import views

urlpatterns=[
    path('',views.watches_world_login),
    path('logout',views.watches_world_shop_logout),

    path('register',views.register),
    path('user_home',views.user_home),
]