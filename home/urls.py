from django.urls import path
from .views import *

urlpatterns = [
    path('index/', HomePage.as_view(), name="home_page"),
]
