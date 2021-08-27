from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name=('register')),
    path('token', views.TokenView.as_view()),
    path('products', views.productList.as_view()),
    path('user/', views.userList.as_view()),
    path('cur/', views.CurView.as_view()),
    path('add/<str:pk>/', views.add),
    path('cart/', views.CartView.as_view()),
    path('remove/<str:pk>/', views.remove),
    path('save/<str:pk>/', views.favourite),
    path('favourite/', views.SaveView.as_view()),
    path('new', views.NewList.as_view()),
]