from django.urls import path
from . import views

urlpatterns = [
    path('', views.booksOverview, name='books-overview'),
    path('books-list/', views.booksList, name='books-list'),
    path('books-detail/<str:pk>/', views.booksDetail, name='books-detail'),
    path('books-create/', views.booksCreate, name='books-create'),
    path('books-update/<str:pk>/', views.booksUpdate, name='books-update'),
    path('books-delete/<str:pk>/', views.booksDelete, name='books-delete'),

    path('', views.checkoutOverview, name='checkout-overview'),
    path('checkout-list/', views.checkoutList, name='checkout-list'),
    path('checkout-detail/<str:pk>/', views.checkoutDetail, name='checkout-detail'),
    path('checkout-create/', views.checkoutCreate, name='checkout-create'),
    path('checkout-update/<str:pk>/', views.checkoutUpdate, name='checkout-update'),
    path('checkout-delete/<str:pk>/', views.checkoutDelete, name='checkout-delete'),
]