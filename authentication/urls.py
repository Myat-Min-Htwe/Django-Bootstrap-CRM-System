from django.urls import path
from .views import RegistrationView,UsernameValidationView,EmailValidationView,LoginView,LogoutView

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', csrf_exempt(RegistrationView.as_view()), name="register"),
    path('login', csrf_exempt(LoginView.as_view()), name="login"),
    path('logout', csrf_exempt(LogoutView.as_view()), name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
]