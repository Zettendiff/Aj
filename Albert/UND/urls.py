from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('collection/', views.collection, name = 'collections'),
    path('sign-up/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),


    path('products/', views.products_list, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    
]