from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('abc',views.abc,name='abc'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('map',views.map,name='map'),
    path('profile',views.profile,name='profile'),
    path('routes',views.routes,name='routes'),
    path('shop',views.shop,name='shop'),
    path('logout',views.LogoutPage,name='logout'),
]

