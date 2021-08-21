from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name=('register')),
    path('token', views.TokenView.as_view()),
    path('products', views.productList.as_view()),
    path('user', views.userList.as_view()),
    path('cur/', views.CurView.as_view()),
    path('cart/<str:pk>/', views.add),
    path('cart', views.CartList.as_view()),
]