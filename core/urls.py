from django.urls import path
from core.views import home, signup

urlpatterns = [
    path("", home, name="home"),
    path("signup", signup, name="signup"),
]
