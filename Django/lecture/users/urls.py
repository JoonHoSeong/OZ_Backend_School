from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', views.Users.as_view()),
    path('myinfo', views.MyInfo.as_view()),
    # Authentication
    #DRF Token
    path('getToken', obtain_auth_token), 
    #Django session login
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view()),
    #JWT Login
    path('login/jwt', views.JWTLogin.as_view()),
    path('login/jwt/info', views.UserDetailView.as_view()),
    #Simple JWT Authentication
    path("login/simple-jwt", TokenObtainPairView.as_view()),
    path("login/simple-jwt/refesh", TokenRefreshView.as_view()),
    path("login/simple-jwt/verify", TokenVerifyView.as_view()),
    
]
