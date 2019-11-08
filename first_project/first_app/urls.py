from django.urls import path
from first_app import views

urlpatterns = [
  path('', views.index, name="index"),
  path('users/', views.users, name="users"),
  path('register/', views.register, name="register")
]