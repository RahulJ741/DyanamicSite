from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$',Login.as_view(),name='login'),
    # re_path('^', Login.as_view(), name='login'),
    path('signup/', SignUP.as_view(), name='signup'),
    path('index/', HomePage.as_view(), name="home_page"),
    path('path/<str:url_path>/', RedirectPage.as_view(), name="redirect_page"),
]
