from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('login', views.login_, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.sign_up, name='signup'),
    path('profile/<slug:usernmae>', views.profile, name='profile'),
path('validateUsername', csrf_exempt(views.validateUsername), name="validateUsername"),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('delete_cart/<int:id>', views.delete_cart, name='delete_cart'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),
         name='reset_password'),
    path('password_reset_sent', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent'
                                                                                       '.html'),
         name='password_reset_sent'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                                'accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name=
                                                                                 'accounts/reset_password_complete.html'),
         name='password_reset_complete'),
]
