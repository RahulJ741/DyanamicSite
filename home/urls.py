from django.urls import path
from .views import *

urlpatterns = [
    path('index/', HomePage.as_view(), name="home_page"),
    path('path/<str:url_path>/', RedirectPage.as_view(), name="redirect_page"),
]
