from django.urls import path
from . import views

urlpatterns =[
    path('get', views.getItems, name='getItems'),
    path('post', views.postItems, name='postItems'),
    path('update/<int:pk>', views.updateItem, name='updateItem'),
    path('delete/<int:pk>', views.deleteItem, name='deleteItem'),
]