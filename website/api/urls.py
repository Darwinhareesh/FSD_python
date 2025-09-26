from django.contrib import admin
from django.urls import path,include
from website.api import views
urlpatterns = [


     path('products/',views.product_list,name='product_list'),
    #  path('api/signup/', views.signup, name='signup'),
    #  path('api/login',views.login, name='login'),
]