"""things URL Configuration

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
from knox import urls

from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views

from users.views import LoginView
from things_backend.urls import router as tb_router
from users.urls import router as users_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(tb_router.urls)),
    path('api/v1/', include(users_router.urls)),
#    path(r'api/v1/auth/', include(urls)),
    path(r'api/v1/login/', LoginView.as_view(), name='knox_login'),
    path(r'api/v1/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'api/v1/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
