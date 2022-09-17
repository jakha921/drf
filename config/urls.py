"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.MenAPIList.as_view()),
    path('api/<int:pk>/', views.MenAPIUpdate.as_view()),
    path('api/delete/<int:pk>/', views.MenAPIDestroy.as_view()),
    path('api/drf/auth/', include('rest_framework.urls')),

    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # JWT refresh token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),      # JWT verify token
]
