from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('Cart/',views.cart, name= 'cart'),
    path('Payment/',views.payment, name= 'payment'),
    path('Profile/',views.profile, name = 'profile'),
]