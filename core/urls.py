from django.urls import path
from core.views import home, signup, user_login, user_logout

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("logout/", user_logout, name="logout"),
    path("login/", user_login, name="login"),
]
