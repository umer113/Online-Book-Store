from django.contrib import admin
from django.urls import path
from .views import index
from . import views
urlpatterns = [
    path('', index,name="home"),
    path('books/',views.books,name = 'books'),
    path('login/',views.login,name ='login'),
    path('signup/',views.signup,name ='signup'),
    path('aboutus/',views.aboutus,name ='aboutus'),
    path('add-to-cart/',views.add_to_cart,name='cart')

]
