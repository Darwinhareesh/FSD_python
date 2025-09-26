from django.contrib import admin
from django.urls import path,include
from website import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('products/', views.product_list, name='products'),
    # path('api/products/',views.product_list,name='product_list'),

    #Dont touch when you are not with me
    path('api/',include('website.api.urls')),
    path('api/signup/', views.signup, name='signup'),
    path('api/login/',views.login, name='login'),
    path('api/add/',views.add_product, name='add_product'),
    path('api/token/',views.get_token, name='get_token'),
]