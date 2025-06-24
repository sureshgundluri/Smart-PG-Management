from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,    # login
    TokenRefreshView        # refresh
)
urlpatterns =[
    path('register/',RegisterView.as_view(),name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('login/',CustomLoginView.as_view(),name='login'),
    path('login_page/',login_page,name="login-page"),
    path('logout/',CustomLogOut.as_view(),name='logout'),
    path('register-page/',register_page,name='register-page'),
    path('dashboard-page/',dashboard_page,name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
