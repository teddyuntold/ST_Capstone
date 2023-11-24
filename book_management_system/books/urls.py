from django.urls import path
from . import views

urlpatterns = [
    path('', views.booksOverview, name='books-overview'),
    path('books-list/', views.booksList, name='books-list'),
    path('books-detail/<str:pk>/', views.booksDetail, name='books-detail'),
    path('books-create/', views.booksCreate, name='books-create'),
    path('books-update/<str:pk>/', views.booksUpdate, name='books-update'),
    path('books-delete/<str:pk>/', views.booksDelete, name='books-delete'),
]