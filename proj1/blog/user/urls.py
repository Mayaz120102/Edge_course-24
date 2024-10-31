from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import register, LogoutView

# restframework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Custom login template
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout path
    path('register/', register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('token/logout/', LogoutView.as_view(), name="token_logout"),
]