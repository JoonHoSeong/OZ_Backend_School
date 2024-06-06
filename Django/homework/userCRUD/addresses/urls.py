from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,TokenVerifyView)

urlpatterns = [
		path('', views.AddressList.as_view(), name='address-list'),
		path('<int:pk>/', views.AddressDetail.as_view(), name='address-detail'),
		path('<int:user_id>/add', views.CreateUserAddress.as_view(), name='create-user-address'),
		path('<int:pk>/update', views.UpdateAddress.as_view(), name='update-address'),
		path('<int:pk>/delete', views.DeleteAddress.as_view(), name='delete-address'),
		path("getToken", obtain_auth_token),
		path("login/simpleJWT", TokenObtainPairView.as_view()),
		path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
		path("login/simpleJWT/verify", TokenVerifyView.as_view())
]