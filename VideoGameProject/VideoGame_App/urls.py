from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_all, name='list_all'),
    path('add/', views.post_new, name='post_new'),
]