from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$',Login.as_view(), name='login'),
    path('signup/', SignUP.as_view(), name='signup'),
    path('home/', ProjectList.as_view(), name='project_list'),
    path('create_project/',ProjectCreation.as_view(),name="create_project"),
    path('detail/<str:slug>/',ProjectDetails.as_view(),name="project_details"),
    path('index/', HomePage.as_view(), name="home_page"),
    path('path/<str:url_path>/', RedirectPage.as_view(), name="redirect_page"),
]
