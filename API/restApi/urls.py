from django.urls import path
from . import views

urlpatterns =[
    path('item/get', views.getItems, name='getItems'),
    path('item/post', views.postItem, name='postItem'),
    path('item/update/<int:pk>', views.updateItem, name='updateItem'),
    path('item/delete/<int:pk>', views.deleteItem, name='deleteItem'),
    path('book/get', views.getBooks, name='getBooks'),
    path('book/post', views.postBook, name='postBook'),
    path('book/update/<int:pk>', views.updateBook, name='updateBook'),
    path('book/delete/<int:pk>', views.deleteBook, name='deleteBook'),
]