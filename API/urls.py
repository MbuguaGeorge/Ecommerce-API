from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name=('register')),
    path('token', views.TokenView.as_view()),
    path('products', views.productList.as_view()),
]