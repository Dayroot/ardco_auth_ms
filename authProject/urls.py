from django.contrib import admin
from django.urls import path
from authApp import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserView.as_view()),
    path('login/', views.UserTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    
]
