# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_index),
    path('<slug:group_name>/', views.group_posts)
]