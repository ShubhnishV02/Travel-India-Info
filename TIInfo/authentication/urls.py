from django.urls import path , include
from . import views



urlpatterns = [
    path('signin/',views.SignIn,name="signin"),
    path('signup/',views.SignUp,name="signup"),
    path('signout/',views.SignOut,name="signout"),


]