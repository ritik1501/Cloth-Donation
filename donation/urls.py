from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="Home"),
    path('addClothes', views.AddClothes.as_view(), name="addClothes"),
    path('contact', views.contact, name="Contact"),

]