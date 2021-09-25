from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.sign_up, name='signup'),
    path('profile/<slug:usernmae>', views.profile, name='profile'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('delete_cart/<int:id>', views.delete_cart, name='delete_cart'),
]
