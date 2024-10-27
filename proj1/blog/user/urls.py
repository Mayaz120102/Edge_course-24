from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import register

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Custom login template
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout path
    path('register/', register, name='register'),
]