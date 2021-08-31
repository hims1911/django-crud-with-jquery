"""PostPublisherProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('products/', include('PostPublisherHome.urls')),
    path('api/register/', views.UserCreate.as_view(), name="create_user"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register', views.register, name="register")
]

from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)