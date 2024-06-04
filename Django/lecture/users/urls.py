from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.Users.as_view()),
    path('myinfo', views.MyInfo.as_view()),
    # Atuthentication
    #DRF Token
    path('getToken', obtain_auth_token), 
    #Django sessoion login
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view()),
    
]
