from django.urls import path
from TIInfo import views
from . import views

urlpatterns = [
    path('gulmarg/',views.Gulmarg,name="gulmarg"),

]