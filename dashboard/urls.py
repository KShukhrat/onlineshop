from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add_category/', add_category, name='add_category'),
    path('delete_category/', delete_category, name='delete_category'),
    path('edit_category/<int:id>/', edit_category, name='edit_category'),
    path('add_product/', add_product, name='add_product'),
    path('billing/', billing, name='billing'),
    path('users/', users, name='users'),
    path('virtual-reality/', virtual_reality, name='virtual-reality'),
    path('profile/', profile, name='profile'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),


    #Users
    path('users/', users, name='users'),
    path('delete_user/', delete_user, name='delete_user'),
    path('edit_user/<int:id>/', edit_user, name='edit_user'),
]